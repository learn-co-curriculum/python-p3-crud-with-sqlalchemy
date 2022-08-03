# Create, Read, Update, and Delete with SQLAlchemy

## Learning Goals

- Learning goal 1.
- Learning goal 2.

***

## Key Vocab

- **Persist**: save a schema in a database.
- **Engine**: a Python object that translates SQL to Python and vice-versa.
- **Session**: a Python object that uses an engine to allow us to
  programmatically interact with a database.
- **Transaction**: a strategy for executing database statements such that
  the group succeeds or fails as a unit.
- **Migration**: the process of moving data from one or more databases to one
  or more target databases.

***

## Introduction

In the previous lesson, we created and persisted a database schema using
SQLAlchemy. This required us to define classes that inherited from a common
`declarative_base` object and that possessed certain attributes that would be
used to assign a table name, columns, primary keys, and more.

In this lesson, we'll be building on the same schema. The code from last
lesson's code-along can be found in `lib/sqlalchemy_sandbox.py`. Run
`chmod +x lib/sqlalchemy_sandbox.py` to make it executable.

> **Note**: we are using a SQLite database in memory now instead of a
> `students.db` file. This will allow us to make changes to our schema without
> running into issues. We will learn how to address changing a schema when we
> discuss **migrations** later in this module.

***

## The Session

SQLAlchemy interacts with the database through **sessions**. These wrap
**engine** objects like the one we included in our script in
`sqlalchemy_sandbox.py`. The session contains an **identity map**, which is
similar to an empty dictionary with keys for the table name, columns, and
primary keys. When the session pulls data from `students.db`, it fills the
identity map and uses it to populate a `Student` object with specific attribute
values. When it commits data to the database, it fills the identity map in the
same fashion but unpacks it into a `students` row instead.

### `sessionmaker`

To create a session, we need to use SQLAlchemy's `sessionmaker` class. This
ensures that there is a consistent identity map for the duration of our session.

Let's create a session in `sqlalchemy_sandbox.py` so that we can start executing
statements in `students.db`:

```py
# lib/sqlalchemy_sandbox.py

# imports
from sqlalchemy.orm import sessionmaker

# data models

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()
```

Run `lib/sqlalchemy_sandbox.py` to persist your schema and create a session.
You won't see anything yet, but it's always wise to stop and check for errors
after you change the functionality of your code.

### Transactions

**Transactions** are a strategy for executing SQL statements via ORM that
ensure that they all succeed or fail as a group. This is especially important
if statements that occur later on depend on earlier statements executing
properly. The workflow for a transaction is illustrated in the image below:

![Workflow for a successful transaction. Shows that after a transaction begins,
the state of the database is recorded, then statements are executed, then the
transaction is committed if all statements are successful.](
https://curriculum-content.s3.amazonaws.com/python/esal_0401.png "successful transaction")

If any of the SQL statements in the above image fail to execute properly,
the database will be rolled back to the state recorded at the beginning of the
transaction and the process will end, returning an error message.

### Refactoring our Schema

Before we begin transactions on our database, let's take a moment to build upon
the `Student` model from the previous lesson:

```py
#!/usr/bin/env python3

# imports
from datetime import datetime
from sqlalchemy import (CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        PrimaryKeyConstraint(
            'student_id',
            name='id_pk'),
        UniqueConstraint(
            'student_email',
            name='unique_email'),
        CheckConstraint(
            'student_grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12'))

    Index('index_student_name', 'student_name')

    student_id = Column(Integer())
    student_name = Column(String())
    student_email = Column(String(55))
    student_grade = Column(Integer())
    student_birthday = Column(DateTime())
    student_enrolled_date = Column(DateTime(), default=datetime.now())

# script
```

Let's break down some of the new features in the `Student` model:

#### Constraints

Along with keys, constraints help ensure that our data meets certain criteria
before being stored in the database. Constraints are stored in the optional
`__table_args__` class attribute. There are three main classes of constraint:

1. `PrimaryKeyConstraint`: assigns primary key status to a `Column`. This can
   also be accomplished through the optional `primary_key` argument to the
   `Column` class constructor.
2. `UniqueConstraint`: checks new records to ensure that they do not match
   existing records at unique `Column`s.
3. `CheckConstraint`: uses SQL statements to check if new values meet
   specific criteria.

Our new constraints for the `Student` model ensure that `student_id` is a
primary key, `student_email` is unique, and `student_grade` is between 1 and
12.

#### Indexes

Indexes are used to speed up lookups on certain column values. Since teachers
and administrators don't typically know their student's ID numbers off the top
of their heads, it's wise to set up an index for `student_name` in preparation
for people using it in their database transactions.

#### Input Sizes, Defaults, and More

SQLAlchemy provides a number of other optional arguments in the `Column` and
data-type constructors that will allow you to make your code more specific and
secure. Explore [the `Column` documentation][column] to learn more.

***

## Creating Records

***

## Lesson Section

Lorem ipsum dolor sit amet. Ut velit fugit et porro voluptas quia sequi quo
libero autem qui similique placeat eum velit autem aut repellendus quia. Et
Quis magni ut fugit obcaecati in expedita fugiat est iste rerum qui ipsam
ducimus et quaerat maxime sit eaque minus. Est molestias voluptatem et nostrum
recusandae qui incidunt Quis 33 ipsum perferendis sed similique architecto.

```py
# python code block
print("statement")
# => statement
```

```js
// javascript code block
console.log("use these for comparisons between languages.")
// => use these for comparisons between languages.
```

```console
echo "bash/zshell statement"
# => bash/zshell statement
```

<details>
  <summary>
    <em>Check for understanding text goes here! <code>Code statements go here.</code></em>
  </summary>

  <h3>Answer.</h3>
  <p>Elaboration on answer.</p>
</details>
<br/>

***

## Conclusion

Conclusion summary paragraph. Include common misconceptions and what students
will be able to do moving forward.

***

## Resources

- [Resource 1](https://www.python.org/doc/essays/blurb/)
- [Reused Resource][reused resource]

[columns]: https://docs.sqlalchemy.org/en/14/core/sqlelement.html
