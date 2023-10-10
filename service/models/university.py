
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


############################################################
#                     University Model
############################################################
class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))

    students = db.relationship('Student', secondary='student_university', back_populates='universities')
    study_areas = db.relationship('StudyArea', secondary='university_study_area', back_populates='universities')
