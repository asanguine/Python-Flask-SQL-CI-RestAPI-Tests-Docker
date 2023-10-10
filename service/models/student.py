
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############################################################
#                     Student Model
############################################################
class Student(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100))
    income = db.Column(db.Integer)

    universities = db.relationship('University', secondary='student_university', back_populates='students')


student_university = db.Table(
    'student_university',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('university_id', db.Integer, db.ForeignKey('university.id'), primary_key=True)
)
