# followers, contacts and friends

## Database relationship

### one-to-many

![1-to-many](http://blog.miguelgrinberg.com/static/images/flask-mega-tutorial-part-iv-2.png)

a user has *many* posts, and a post has *one* user. The relationship is represented in the database with the use of a *foreign key* on the "many" side.

### many-to-many

As an example, consider a database that has `students` and `teachers`. 

We can say that a student has many teachers, and a teacher has many students.

The representation of a many-to-many relationship requires the use of an auxiliary table called an `association table`. Here is how the database would look for the students and teachers example:

![many-to-many](http://blog.miguelgrinberg.com/static/images/flask-mega-tutorial-part-viii-1.png)

While it may not seem straightforward, the association table with its two foreign keys is able to efficiently answer many types of queries, such as:

- Who are the teachers of student S?
- Who are the students of teacher T?
- How many students does teacher T have?
- How many teachers does student S have?
- Is teacher T teaching student S?
- Is student S in teacher T's class?

### one-to-one

A one-to-one relationship is a special case of a one-to-many. The representation is similar, but a constrain is added to the database to prevent the "many" side to have more than one link.

## Representing followers and followed

A relationship in which instances of an entity are linked to other instances of the same entity is called a `self-referential relationship`, and that is exactly what we need here.

![followers](http://blog.miguelgrinberg.com/static/images/flask-mega-tutorial-part-viii-2.png)

```python
followed = db.relationship('User', 
                               secondary=followers, 
                               primaryjoin=(followers.c.follower_id == id), 
                               secondaryjoin=(followers.c.followed_id == id), 
                               backref=db.backref('followers', lazy='dynamic'), 
                               lazy='dynamic')
```

We define the relationship as seen from the left side entity with the name `followed`, because when we query this relationship from the left side we will get the list of followed users. Let's examine all the arguments to the `db.relationship()` call one by one:

- `'User'` is the right side entity that is in this relationship (the left side entity is the parent class). Since we are defining a self-referential relationship we use the same class on both sides.
- `secondary` indicates the association table that is used for this relationship.
- `primaryjoin` indicates the condition that links the left side entity (the follower user) with the association table. Note that because the followers table is not a model there is a slightly odd syntax required to get to the field name.
- `secondaryjoin` indicates the condition that links the right side entity (the followed user) with the association table.
- `backref` defines how this relationship will be accessed from the right side entity. We said that for a given user the query named `followed` returns all the right side users that have the target user on the left side. The back reference will be called `followers` and will return all the left side users that are linked to the target user in the right side. The additional lazy argument indicates the execution mode for this query. A mode of dynamic sets up the query to not run until specifically requested. This is useful for performance reasons, and also because we will be able to take this query and modify it before it executes. More about this later.
- `lazy` is similar to the parameter of the same name in the backref, but this one applies to the regular query instead of the back reference.

## Adding and removing 'follows'

To promote reusability, we will implement the `follow` and `unfollow`
functionality in the `User` model instead of doing it directly in the view
functions.

That way we can use this feature for the actual application (invoking it from the view functions) and also from our unit testing framework.

These methods are amazingly simple, thanks to the power of sqlalchemy who does a lot of work under the covers. We just add or remove items from the followed relationship and sqlalchemy takes care of managing the association table for us.

The follow and unfollow methods are defined so that they return an `object` when they succeed or `None` when they fail. 

When an object is returned, this object **has to be** added to the database session and committed.

### query object

The is_following method does a lot in its single line of code. We are taking the followed relationship query, which returns all the (follower, followed) pairs that have our user as the follower, and we filter it by the followed user. This is possible because the followed relationship has a lazy mode of dynamic, so instead of being the result of the query, this is the actual query object, before execution.

The return from the filter call is the modified query, still without having executed. So we then call count() on this query, and now the query will execute and return the number of records found. If we get one, then we know a link between these two uses is already present. If we get none then we know a link does not exist.

## Database queries

Index page should show the posts written by all the people that are followed by the
logged in user.

return query object not result

> Note the usage of the `followed_posts()` method. This method returns a query object, not the results. This is similar to how relationships with lazy = 'dynamic' work. It is always a good idea to return query objects instead of results, because that gives the caller the choice of adding more clauses to the query before it is executed.

- `all()`
- `count()`
- `first()`

## Possible features

- `block` one more many-to-many relationship and join+filter query
- `group` 
