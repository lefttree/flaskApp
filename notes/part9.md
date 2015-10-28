# Pagination

## post blog

- `forms.py` add `PostForm`
- `index.html`
- `views.py` index view

`posts = g.user.followed_posts().all()`

## pagination

`posts = g.user.followed_posts().paginate(1, 3, False).items`

`Paginate` object

- `has_next`
- `has_prev`
- `next_num`
- `prev_num`
