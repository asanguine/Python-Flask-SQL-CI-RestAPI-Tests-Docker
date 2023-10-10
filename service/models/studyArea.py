
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############################################################
#                     StudyArea Model
############################################################
class StudyArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    universities = db.relationship('University', secondary='university_study_area', back_populates='study_areas')

