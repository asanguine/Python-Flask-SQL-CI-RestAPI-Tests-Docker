
import logging
from flask_sqlalchemy import SQLAlchemy
from service import db

logger = logging.getLogger()
#db = SQLAlchemy()


class DataValidationError(Exception):
    """Used for an data validation errors when deserializing"""


############################################################
#                     Student Model
############################################################
class Student(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone_number = db.Column(db.Integer)
    major = db.Column(db.String(100))
    budget = db.Column(db.Integer)
    status = db.Column(db.String(100))
    assigned_university = db.Column(db.String(100))

    universities = db.relationship('University', secondary='student_university', back_populates='students')


    def __repr__(self):
        return '<Student %r>' % self.name

    def to_dict(self) -> dict:
        """Serializes the class as a dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_dict(self, data: dict) -> None:
        """Sets attributes from a dictionary"""
        for key, value in data.items():
            setattr(self, key, value)

    def create(self):
        """Creates a Student in the database"""
        logger.info("Creating %s", self.name)
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates a Student in the database"""
        logger.info("Saving %s", self.name)
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        """Removes an Account from the database"""
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()


############################################################
#                     StudyArea Model
############################################################
class StudyArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    universities = db.relationship('University', secondary='university_study_area', back_populates='study_areas')



############################################################
#                     University Model
############################################################
class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))

    students = db.relationship('Student', secondary='student_university', back_populates='universities')
    study_areas = db.relationship('StudyArea', secondary='university_study_area', back_populates='universities')



############################################################
#         student - university relationship                 =================================
############################################################

student_university = db.Table(
    'student_university',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('university_id', db.Integer, db.ForeignKey('university.id'), primary_key=True)
)

############################################################
#         study area - university relationship              =================================
############################################################

university_study_area = db.Table(
    'university_study_area',
    db.Column('university_id', db.Integer, db.ForeignKey('university.id'), primary_key=True),
    db.Column('study_area_id', db.Integer, db.ForeignKey('study_area.id'), primary_key=True)
)


############################################################
#                   Accommodation Model
############################################################
PREDEFINED_ACCOMMODATION_TYPES = [
    'Hotel',
    'Airbnb',
    'Private Dorm',
    'School Dorm',
    'Apartment',
]

class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # Example: Hotel, Dormitory, etc.
    price = db.Column(db.Integer)
    location = db.Column(db.String(100))
