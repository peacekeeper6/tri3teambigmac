""" database dependencies to support Users db examples """

from __init__ import db
from sqlalchemy.exc import IntegrityError
# from flask_login import UserMixin

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''


# Define the 'Users Notes' table  with a relationship to Users within the model
# Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class.
# A Foreign key is a column that creates a relationship between two tables. The purpose of the Foreign key is to maintain data integrity and allow navigation between two different instances of an entity. It acts as a cross-reference between two tables as it references the primary key of another table(Users in our case). Every relationship in the database should be supported by a foreign key.

class Timeline(db.Model):
    __tablename__ = 'timeline'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, unique=False, nullable=False)
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    timestamp = db.Column(db.Text, unique=False, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    access = db.Column(db.Integer, unique=False, nullable=False)

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, content, timestamp, userID, access):
        self.content = content
        self.timestamp = timestamp
        self.userID = userID
        self.access = access

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Timeline(" + str(self.id) + "," + self.content + "," + self.timestamp + "," + str(self.userID) + "," + str(self.access) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp,
            "userID": self.userID,
            "access": self.access
        }


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL