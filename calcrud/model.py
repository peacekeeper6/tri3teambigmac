""" database dependencies to support Users db examples """

from __init__ import db
from sqlalchemy.exc import IntegrityError
# from flask_login import UserMixin

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''


# Define the 'Users Notes' table  with a relationship to Users within the model
# Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class.
# A Foreign key is a column that creates a relationship between two tables. The purpose of the Foreign key is to maintain data integrity and allow navigation between two different instances of an entity. It acts as a cross-reference between two tables as it references the primary key of another table(Users in our case). Every relationship in the database should be supported by a foreign key.

class Calendar(db.Model):
    __tablename__ = 'calendar'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, unique=False, nullable=False)
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    content2 = db.Column(db.Text, unique=False, nullable=False)
    content3 = db.Column(db.Text, unique=False, nullable=False)
    content4 = db.Column(db.Text, unique=False, nullable=False)
    content5 = db.Column(db.Text, unique=False, nullable=False)
    content6 = db.Column(db.Text, unique=False, nullable=False)
    content7 = db.Column(db.Text, unique=False, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, content, content2, content3, content4, content5, content6, content7, userID):
        self.content = content
        self.content2 = content2
        self.content3 = content3
        self.content4 = content4
        self.content5 = content5
        self.content6 = content6
        self.content7 = content7
        self.userID = userID

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Calendar(" + str(self.id) + "," + self.content + "," + self.content2 + "," + self.content3 + "," + "," + self.content4 + "," + self.content5 + "," + self.content6 + "," + self.content7 + "," + str(self.userID) + ")"

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
            "content2": self.content2,
            "content3": self.content3,
            "content4": self.content4,
            "content5": self.content5,
            "content6": self.content6,
            "content7": self.content7,
            "userID": self.userID
        }