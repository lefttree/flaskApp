from flask import render_template, flash, redirect, session, url_for, request, g
from flask import jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.babel import lazy_gettext
from flask.ext.sqlalchemy import get_debug_queries
from app import app, db, lm, babel
from .forms import LoginForm, EditForm, PostForm
from .models import User, Post, Note
from oauth import OAuthSignIn
from datetime import datetime
from config import POSTS_PER_PAGE, LANGUAGES, DATABASE_QUERY_TIMEOUT
from .emails import follower_notification
from guess_language import guessLanguage
from .translate import microsoft_translate


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods=['GET', 'POST'])
@login_required  # add login_required
def index(page=1):
    # add page argument
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(), author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(lazy_gettext('Your post is now live!'))
        return redirect(url_for('index'))  # avoid re-submiting
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html',
                            title='Home',
                            posts=posts,
                            form=form)


# @app.route('/login', methods=['GET', 'POST'])
# @oid.loginhandler  # tells Flask-OpenID this is our login view function
# def login():
    # if g.user is not None and g.user.is_authenticated:
        # return redirect(url_for('index'))  # clean than redirect('/index')
    # form = LoginForm()
    # # handle submitted form data
    # # validate_on_submit() will run all the validators and return boolean
    # if form.validate_on_submit():
        # session['remember_me'] = form.remember_me.data
        # return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    # return render_template('login.html',
                            # title='Sign In',
                            # form=form,
                            # providers=app.config['OPENID_PROVIDERS'])

# loads a user from database, used by Flask-Login
# user ids in Flask-Login are always unicode strings, so convert to int is necessary
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


# @oid.after_login
# def after_login(resp):
    # # validation
    # if resp.email is None or resp.email == "":
        # flash('Invalid login. Please try again.')
        # return redirect(url_for('login'))
    # # search our database for the user
    # user = User.query.filter_by(email=resp.email).first()
    # # if not found, this is a new user, add into databse
    # if user is None:
        # nickname = resp.nickname
        # if nickname is None or nickname == "":
            # nickname = resp.email.split('@')[0]
        # user = User(nickname=nickname, email=resp.email)
        # db.session.add(user)
        # db.session.commit()
    # remember_me = False
    # if 'remember_me' in session:
        # remember_me = session['remember_me']
        # session.pop('remember_me', None)
    # login_user(user, remember=remember_me)
    # return redirect(request.args.get('next') or url_for('index'))


# Any function decorated with before_request will run before
# the view function
# `current_user` is set by Flask-Login, so store it in g.user
@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.locale = get_locale()

@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= DATABASE_QUERY_TIMEOUT:
            app.logger.Warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (query.statement, query.parameters, query.duration, query.context))

    return response


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#################################
# OAuth views
#################################

@app.route('/oauth')
def oauth():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index')) # clean than redirect('/index')
    return render_template('oauth.html')


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not g.user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not g.user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email, avatarLarge, avatarSmall = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        nickname = User.make_unique_nickname(username)
        user = User(social_id=social_id, nickname=nickname, email=email, avatarLarge=avatarLarge, avatarSmall=avatarSmall)
        db.session.add(user)
        db.session.commit()
        # follow him/herself
        db.session.add(user.follow(user))
        db.session.commit()
    else:
        u = user.follow(user)
        if u:
            db.session.add(u)
            db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(url_for('index'))

# User profile view
@app.route('/user/<nickname>')
@app.route('/user/<nickname>/<int:page>')
@login_required
def user(nickname, page=1):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = user.sorted_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',
                            user=user,
                            posts=posts)

# User about_me edit view
@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash(lazy_gettext('Your changes have been saved.'))
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)

@app.route('/user_list')
@login_required
def user_list():
    users = User.query.all()
    if users == None:
        flash('No user are found!')
        return redirect(url_for('index'))
    return render_template('user_list.html', users=users)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    #roll database back to a working session
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t follow yourself!')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.follow(user)
    if u is None:
        flash('Cannot follow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You are now following ' + nickname + '!')
    return redirect(url_for('user', nickname=nickname))

@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t unfollow yourself!')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash('Cannot unfollow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You have stopped following ' + nickname + '.')
    follower_notification(user, g.user)
    return redirect(url_for('user', nickname=nickname))

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route('/translate', methods=['POST'])
@login_required
def translate():
    return jsonify({
        'text': microsoft_translate(
            request.form['text'],
            request.form['sourceLang'],
            request.form['destLang']
            )
        })

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)
    if post is None:
        flash(lazy_gettext('Post not found.'))
        return redirect(url_for('index'))
    if post.author.id != g.user.id:
        flash(lazy_gettext('You cannot delete this post!'))
        return redirect(url_for('index'))
    db.session.delete(post)
    db.session.commit()
    flash(lazy_gettext('Your post has been deleted.'))
    return redirect(url_for('index'))

@app.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        if request.form.get('content'):
            note = Note(content=request.form['content'], timestamp=datetime.utcnow(), note_author=g.user)
            db.session.add(note)
            db.session.commit()
            print(note)
            rendered = render_template('note.html', note=note)
            return jsonify({'note': rendered, 'success': True})
        return jsonify({'success': False})
    user = g.user
    notes = user.sorted_notes().all()
    print(notes)
    return render_template('notes.html', notes=notes)
    
    # notes = Note.public().limit(50)
    # # notes = []
    # return render_template('index.html', note=notes)


@app.route('/archive/<int:pk>', methods=['GET', 'POST'])
def archive(pk):
    note = Note.query.filter_by(id=pk).first()
    if note is None:
        return redirect(url_for('notes'))
    note.archived = True
    db.session.add(note)
    db.session.commit()
    return jsonify({'success': True})
