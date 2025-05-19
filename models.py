from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    studentid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dob = db.Column(db.Date)

class Course(db.Model):
    __tablename__ = 'course'
    courseid = db.Column(db.Integer, primary_key=True)
    coursename = db.Column(db.String(100))
    credits = db.Column(db.Integer)
    lecturerid = db.Column(db.Integer)

class Marks(db.Model):
    __tablename__ = 'marks'
    markid = db.Column(db.Integer, primary_key=True)
    studentid = db.Column(db.Integer)
    courseid = db.Column(db.Integer)
    score = db.Column(db.Float)

class Attendance(db.Model):
    __tablename__ = 'attendance'
    attendanceid = db.Column(db.Integer, primary_key=True)
    studentid = db.Column(db.Integer)
    courseid = db.Column(db.Integer)
    date = db.Column(db.Date)
    status = db.Column(db.String(10))