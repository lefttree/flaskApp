# Database

## ORM

- `Flask-SQLAlchemy`

ORMs allow database app to work with objects instead of tables and SQL. The operations
preformed on the objects are translated into database commands by the ORM.

## Migration

- `SQLAlchemy-migrate`

To keep track of database updates for us.

## Configuration

For our little application we will use a `sqlite` database. The `sqlite` databases are the most convenient choice for small applications, as each database is stored in a `single file` and there is no need to start a database server.

- Add `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_MIGRATE_REPO` in `config.py`.
- `SQLALCHEMY_DATABASE_URI` is required by the Flask-SQLAlchemy extension, the path of our database file
- `SQLALCHEMY_MIGRATE_REPO` is the folder where we will store the SQLAlchemy-migrate data files
- init databse in `__init__.py`

## The databse model

use [WWW SQL Designer](http://ondras.zarovi.cz/sql/demo) to design the table.

`app/models.py`

## Creating the database

`db_create.py`

## First Migration

We will consider any changes to the structure of the app database a *migration*.
So from empty databse to a databse that can store users, it's the first migration.

The script looks complicated, but it doesn't really do much. The way SQLAlchemy-migrate creates a migration is by comparing the structure of the database (obtained in our case from file `app.db`) against the structure of our models (obtained from file `app/models.py`). The differences between the two are recorded as a migration script inside the migration repository. 

The migration script knows how to apply a migration or undo it, so it is always possible to upgrade or downgrade a database format.

To make it easy for SQLAlchemy-migrate to determine the changes I never rename existing fields, I limit my changes to adding or removing models or fields, or changing types of existing fields. And I always review the generated migration script to make sure it is right.

## Database upgrades and downgrades

If you have database migration support, then when you are ready to release the new version of the app to your production server you just need to record a new migration, copy the migration scripts to your production server and run a simple script that applies the changes for you.

- `db_upgrade.py`
- `db_downgrade.py`

## Database relationships

![relational db](http://blog.miguelgrinberg.com/static/images/flask-mega-tutorial-part-iv-2.png)

`post` has a `foreign key` id linked to `user`

Modify `app/models.py`

Note that we have also added a new field to `User` class called `posts`. It's not a actual field.
For a one-to-many relationship a `db.relationship` field is normally defined on the "one" side.

With this relationship we get a `user.posts` member that gets us the list of posts from the user. The first argument to `db.relationship` indicates the "many" class of this relationship. The `backref` argument defines a `field` that will be added to the objects of the "many" class that points back at the "one" object.

## Play with db

- `query.all()`
- `query.get(id)`

refer to [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/index.html) to see the options to query the database.


