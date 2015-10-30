# Deployment

## Heroku

- register on heroku
- install [Heroku tolbelt](https://toolbelt.heroku.com/)
- git setup

Heroku looks for a file called `Procfile` and `requirements.txt`

## Eliminating local file storage

Applications that run on Heroku are not supposed to write permanent files to disk, because Heroku uses a virtualized platform that does not remember data files, the file system is reset to a clean state that just contains the application script files each time a virtual worker is started.

Functions affected:

- sqlite
- full text search
- translation files
- logging

1. use heroku's database offering
2. disable full text search for now
3. include the compiled translation files in the git repository
4. add our logs to the logger that heroku uses

## requirements file

`pip freeze > requirements.txt`

## Procfile

```
web: gunicorn app:app
init: python db_create.py
upgrade: python db_upgrade.py
```

## Deploy 

### push

to push our app to the heroku, just `git push heroku master`

### first time run

`heroku run init`

### update

`git push` then `heroku run upgrade`

### logging

`heroku logs` to see all the logs
`heroku logs --source app` to see only app related logs

