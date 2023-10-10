
import logging
from datetime import date
from flask_sqlalchemy import SQLAlchemy
#from service import db

#logger = logging.getLogger("flask.app")
logger = logging.getLogger()

#db = SQLAlchemy()

class DataValidationError(Exception):
    """Used for an data validation errors when deserializing"""




######################################################################
#  P E R S I S T E N T   B A S E   M O D E L
######################################################################
# class PersistentBase:
#     """Base class added persistent methods"""

#     def __init__(self):
#         self.id = None  # pylint: disable=invalid-name

#     def create(self):
#         """
#         Creates a Account to the database
#         """
#         logger.info("Creating %s", self.name)
#         self.id = None  # id must be none to generate next primary key
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         """
#         Updates a Account to the database
#         """
#         logger.info("Updating %s", self.name)
#         db.session.commit()

#     def delete(self):
#         """Removes a Account from the data store"""
#         logger.info("Deleting %s", self.name)
#         db.session.delete(self)
#         db.session.commit()

#     @classmethod
#     def init_db(cls, app):
#         """Initializes the database session"""
#         logger.info("Initializing database")
#         cls.app = app
#         # This is where we initialize SQLAlchemy from the Flask app
#         db.init_app(app)
#         app.app_context().push()
#         db.create_all()  # make our sqlalchemy tables

#     @classmethod
#     def all(cls):
#         """Returns all of the records in the database"""
#         logger.info("Processing all records")
#         return cls.query.all()

#     @classmethod
#     def find(cls, by_id):
#         """Finds a record by it's ID"""
#         logger.info("Processing lookup for id %s ...", by_id)
#         return cls.query.get(by_id)



############################################################
#                     Student Model
############################################################
# class Student(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     major = db.Column(db.String(100))
#     income = db.Column(db.Integer)

#     universities = db.relationship('University', secondary='student_university', back_populates='students')


# student_university = db.Table(
#     'student_university',
#     db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
#     db.Column('university_id', db.Integer, db.ForeignKey('university.id'), primary_key=True)
# )


############################################################
#                     StudyArea Model
############################################################
# class StudyArea(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

#     universities = db.relationship('University', secondary='university_study_area', back_populates='study_areas')


############################################################
#                     University Model
############################################################
# class University(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     location = db.Column(db.String(100))

#     students = db.relationship('Student', secondary='student_university', back_populates='universities')
#     study_areas = db.relationship('StudyArea', secondary='university_study_area', back_populates='universities')

############################################################
#                   Accommodation Model
############################################################
# class Accommodation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     type = db.Column(db.String(50))  # Example: Hotel, Dormitory, etc.
#     price = db.Column(db.Integer)
#     location = db.Column(db.String(100))

# PREDEFINED_ACCOMMODATION_TYPES = [
#     'Hotel',
#     'Airbnb',
#     'Private Dorm',
#     'School Dorm',
#     'Apartment',
# ]



# def init_db(app):
#     """Initialize the SQLAlchemy app"""
#     Student.init_db(app)