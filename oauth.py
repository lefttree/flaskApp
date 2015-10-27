from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session

class OAuthSignIn(object):
    """
    Defines the structure that the subclasses that implement each provider
    must follow
    """
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        """
        Init the authentication process
        redirect to the provider's site to authenticate
        """
        pass

    def callback(self):
        """
        provider redirects back
        """
        pass

    def get_callback_url(self):
        return url_for('oauth_callback', provider=self.provider_name, _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
                    name = 'facebook',
                    client_id = self.consumer_id,
                    client_secret = self.consumer_secret,
                    authorize_url = 'https://graph.facebook.com/oauth/authorize',
                    access_token_url = 'https://graph.facebook.com/oauth/access_token',
                    base_url = 'https://graph.facebook.com/'
                )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
                scope = 'email',
                response_type= 'code',
                redirect_uri = self.get_callback_url()
            ))

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data = {
                'code': request.args['code'],
                'grant_type': 'authorization_code',
                'redirect_uri': self.get_callback_url()
                }
        )
        me = oauth_session.get('me').json()
        print("-----------------------")
        print(me)
        avatarLarge = oauth_session.get('https://graph.facebook.com/' + me['id'] + '?fields=picture.type(large)', params={'format': 'json'})
        avatarSmall = oauth_session.get('https://graph.facebook.com/' + me['id'] + '?fields=picture.type(small)', params={'format': 'json'})
        return (
            'facebook$' + me['id'],
            # me.get('email').split('@')[0],
            # me.get('email')
            me.get('name'),
            me.get('name') + "@facebook.com",
            avatarLarge.json()['picture']['data']['url'],
            avatarSmall.json()['picture']['data']['url']
        )

# class TwitterSignIn(OAuthSignIn):
    # pass
