""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from __init__ import app
import json

app_oceanquiz = Blueprint('oceanquiz', __name__,
                         url_prefix='/oceanquiz',
                         template_folder='templates/oceanquiz/',
                         static_folder='static',
                         static_url_path='static')

@app_oceanquiz.route('/')
def oceanquiz():
        # questionID = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8',
        #          'question9', 'question10']

        questions = [{"question": "What percent of the United States is underneath the oceans?",
                    "a": "A: 40%",
                    "b": "B: 50%",
                    "c": "C: 60%",
                    "d": "D: 70",
                    "correctAnswer": "b"},
                   {"question": "Over what percent of our planet's oxygen levels are produced by the ocean?",
                    "a": "A: Over 50%",
                    "b": "B: Over 60%",
                    "c": "C: Over 70%",
                    "d": "D: Over 80%",
                    "correctAnswer": "c"},
                   {"question": "About how many islands does the Pacific Ocean contain?",
                    "a": "A: 25,000",
                    "b": "B: 30,000",
                    "c": "C: 40,000",
                    "d": "D: 7",
                    "correctAnswer": "a"},
                   {"question": " How many people have set foot on the Mariana Trench (lowest point in the ocean)?",
                    "a": "A: 1",
                    "b": "B: 2",
                    "c": "C: 3",
                    "d": "D: 4",
                    "correctAnswer": "c"},
                   {"question": "About how many shipwrecks are in the oceans?",
                    "a": "A: 3,000,000",
                    "b": "B: 4,000,000",
                    "c": "C: 5,000,000",
                    "d": "D: 6,000,000",
                    "correctAnswer": "a"},
                   {"question": "How deep is the Mariana Trench?",
                    "a": "A: 6 miles",
                    "b": "B: 6.5 miles",
                    "c": "C: 7 miles",
                    "d": "D: 7.5 miles",
                    "correctAnswer": "c"},
                   {"question": "How long was the largest blue whale ever recorded?",
                    "a": "A: 108 feet",
                    "b": "B: 118 feet",
                    "c": "C: 128 feet",
                    "d": "D: 138 feet",
                    "correctAnswer": "a"},
                   {"question": "What is the largest ocean on Earth?",
                    "a": "A: Atlantic",
                    "b": "B: Indian",
                    "c": "C: Asian",
                    "d": "D: Pacific",
                    "correctAnswer": "d"},
                   {"question": "What is the average depth of the ocean?",
                    "a": "A: 11,100 feet",
                    "b": "B: 12,100 feet",
                    "c": "C: 13,100 feet",
                    "d": "D: 14,100 feet",
                    "correctAnswer": "b"},
                   {"question": "Where was the world record for deepest freedive set?",
                    "a": "A: Russia",
                    "b": "B: Greece",
                    "c": "C: Indonesia",
                    "d": "D: Peru",
                    "correctAnswer": "b"}]
        # d = dict(zip(questionID, questions))
        # json_object = json.dumps(d, indent=4)
        return render_template('oceanquiz/templates/oceanquiz.html', questions=questions)
        # print(d)
# main()
# # Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# # Define variable to define type of database (sqlite), and name and location of myDB.db
# dbURI = 'sqlite:///model/myDB.db'
# # Setup properties for the database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
# app.config['SECRET_KEY'] = 'SECRET_KEY'
# # Create SQLAlchemy engine to support SQLite dialect (sqlite:)
# db = SQLAlchemy(app)
# Migrate(app, db)
#
# hello = [
#         ['emp1', 'emp2', 'emp3'],
#         ]
#
# EmpInfo = [{'name': 'Bob', 'job': 'Mgr'},
#            {'name': 'Kim', 'job': 'Dev'},
#            {'name': 'Sam', 'job': 'Dev'}]
# D = dict(zip(hello, EmpInfo))
# print(D)

# data = {
# "question1": {
#         "question": "Over what percent of our planet's oxygen levels are produced by the ocean?",
#         "a": "Over 50%",
#         "b": "Over 60%",
#         "c": "Over 70%",
#         "d": "Over 80%",
#         "correctAnswer": "c",
# },
# "question2": {
#         "question": "What percent of the United States is underneath the oceans?",
#         "a": "40%",
#         "b": "50%",
#         "c": "60%",
#         "d": "70",
#         "correctAnswer": "b",
# },
# "question3": {
#         "question": "About how many islands does the Pacific Ocean contain?",
#         "a": "25,000",
#         "b": "30,000",
#         "c": "40,000",
#         "d": "7",
#         "correctAnswer": "a",
# },
# "question4": {
#         "question": " How many people have set foot on the Mariana Trench (lowest point in the ocean)?",
#         "a": "1",
#         "b": "2",
#         "c": "3",
#         "d": "4",
#         "correctAnswer": "c",
# },
# "question5": {
#         "question": "About how many shipwrecks are in the oceans?",
#         "a": "3,000,000",
#         "b": "4,000,000",
#         "c": "5,000,000",
#         "d": "6,000,000",
#         "correctAnswer": "a",
# },
# "question6": {
#         "question": "How deep is the Mariana Trench?",
#         "a": "6 miles",
#         "b": "6.5 miles",
#         "c": "7 miles",
#         "d": "7.5 miles",
#         "correctAnswer": "c",
# },
# "question7": {
#         "question": "How long was the largest blue whale ever recorded?",
#         "a": "108 feet",
#         "b": "118 feet",
#         "c": "128 feet",
#         "d": "138 feet",
#         "correctAnswer": "a",
# },
# "question8": {
#         "question": "What is the largest ocean on Earth?",
#         "a": "Atlantic",
#         "b": "Indian",
#         "c": "Asian",
#         "d": "Pacific",
#         "correctAnswer": "d",
# },
# "question9": {
#         "question": "What is the average depth of the ocean?",
#         "a": "11,100 feet",
#         "b": "12,100 feet",
#         "c": "13,100 feet",
#         "d": "14,100 feet",
#         "correctAnswer": "b",
# },
# "question10": {
#         "question": "Where was the world record for deepest freedive set?",
#         "a": "Russia",
#         "b": "Greece",
#         "c": "Indonesia",
#         "d": "Peru",
#         "correctAnswer": "b"
# }}



#         "questionID": "1",
#         "question": "Over what percent of our planet's oxygen levels are produced by the oceans?",
#         "a": "Over 50%",
#         "b": "Over 60%",
#         "c": "Over 70%",
#         "d": "Over 80%",
#         "correctAnswer": "c",
#         "questionID": "2",
#         "question": "What percent of the United States is underneath the oceans?",
#         "a": "40%",
#         "b": "50%",
#         "c": "60%",
#         "d": "70",
#         "correctAnswer": "b",
#         "questionID": "3",
#         "question": "About how many islands does the Pacific Ocean contain?",
#         "a": "25,000",
#         "b": "30,000",
#         "c": "40,000",
#         "d": "7",
#         "correctAnswer": "a",
#         "questionID": "4",
#         "question": " How many people have set foot on the Mariana Trench (lowest point in the ocean)?",
#         "a": "1",
#         "b": "2",
#         "c": "3",
#         "d": "4",
#         "correctAnswer": "c",
#         "questionID": "5",
#         "question": "About how many shipwrecks are in the oceans?",
#         "a": "3,000,000",
#         "b": "4,000,000",
#         "c": "5,000,000",
#         "d": "6,000,000",
#         "correctAnswer": "a",
#         "questionID": "6",
#         "question": "How deep is the Mariana Trench?",
#         "a": "6 miles",
#         "b": "6.5 miles",
#         "c": "7 miles",
#         "d": "7.5 miles",
#         "correctAnswer": "c",
#         "questionID": "7",
#         "question": "How long was the largest blue whale ever recorded?",
#         "a": "108 feet",
#         "b": "118 feet",
#         "c": "128 feet",
#         "d": "138 feet",
#         "correctAnswer": "a",
#         "questionID": "8",
#         "question": "What is the largest ocean on Earth?",
#         "a": "Atlantic",
#         "b": "Indian",
#         "c": "Asian",
#         "d": "Pacific",
#         "correctAnswer": "d",
#         "questionID": "9",
#         "question": "What is the average depth of the ocean?",
#         "a": "11,100 feet",
#         "b": "12,100 feet",
#         "c": "13,100 feet",
#         "d": "14,100 feet",
#         "correctAnswer": "b",
#         "questionID": "10",
#         "question": "Where was the world record for deepest freedive set?",
#         "a": "Russia",
#         "b": "Greece",
#         "c": "Indonesia",
#         "d": "Peru",
#         "correctAnswer": "b"
# }




# json_object = json.dumps(data, indent=4)
# print(json_object)

# f = open('templates/oceanquiz/js/questions.js',)
# data = json.load(f)
# type(data)


# def oceanquiz():
#     for i in range(len(json_object)):
#         print(json_object[i]["question"])
    # return render_template('templates/oceanquiz/templates/oceanquiz.html', json_object)

# oceanquiz()
# class questions(db.Model):
#     questionID = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.Text, unique=False, nullable=False)
#     a = db.Column(db.Text, unique=False, nullable=False)
#     b = db.Column(db.Text, unique=False, nullable=False)
#     c = db.Column(db.Text, unique=False, nullable=False)
#     d = db.Column(db.Text, unique=False, nullable=False)
#     correctAnswer = db.Column(db.Text, unique=False, nullable=False)
#
#     def __init__(self, question, a, b, c, d, correctAnswer):
#         self.question = question
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.correctAnswer = correctAnswer
#
#     # CRUD create/add a new record to the table
#     # returns self or None on error
#     def create(self):
#         try:
#             # creates a person object from Users(db.Model) class, passes initializers
#             db.session.add(self)  # add prepares to persist person object to Users table
#             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None
#
#     # CRUD read converts self to dictionary
#     # returns dictionary
#     def read(self):
#         return {
#             "questionID": self.questionID,
#             "question": self.question,
#             "a": self.a,
#             "b": self.b,
#             "c": self.c,
#             "d": self.d,
#             "correctAnswer": self.correctAnswer
#         }
#
#     # CRUD update: updates users name, description, usertag
#     # returns self
#     def update(self, question="", a="", b="", c="", d="", correctAnswer=""):
#         if len(question) > 0:
#             self.question = question
#         if len(a) > 0:
#             self.a = a
#         if len(b) > 0:
#             self.b = b
#         if len(c) > 0:
#             self.c = c
#         if len(d) > 0:
#             self.d = d
#         if len(correctAnswer) > 0:
#             self.correctAnswer = correctAnswer
#         db.session.commit()
#         return self
#
#     # CRUD delete: remove self
#     # None
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#         return None
