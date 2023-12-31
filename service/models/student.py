
import logging
from flask_sqlalchemy import SQLAlchemy
from service import db

logger = logging.getLogger()

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
    budget = db.Column(db.Integer)
    status = db.Column(db.String(100))

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

    def __init__(self, name):
        self.name = name


############################################################
#                 Language Model
############################################################
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_hardcoded_languages():
        english = Language(name='English')
        german = Language(name='German')

        db.session.add(english)
        db.session.add(german)
        db.session.commit()

############################################################
#                     University Model
############################################################
class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))

    def __repr__(self):
        return f'<University {self.name}>'


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



# =============== RELATIONSHIP TABLES =================

############################################################
#         study area - university relationship              =================================
############################################################
university_study_area = db.Table(
    'university_study_area',
    db.Column('university_id', db.Integer, db.ForeignKey('university.id'), primary_key=True),
    db.Column('study_area_id', db.Integer, db.ForeignKey('study_area.id'), primary_key=True)
)


############################################################
#         study area - language relationship                =================================
############################################################
language_study_area = db.Table(
    'language_study_area',
    db.Column('language_id', db.Integer, db.ForeignKey('language.id'), primary_key=True),
    db.Column('study_area_id', db.Integer, db.ForeignKey('study_area.id'), primary_key=True)
)


############################################################
#         student - language relationship                   =================================
############################################################
language_student = db.Table(
    'language_student',
    db.Column('language_id', db.Integer, db.ForeignKey('language.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
)


############################################################
#         study area - student relationship                 =================================
############################################################
student_study_area = db.Table(
    'student_study_area',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('study_area_id', db.Integer, db.ForeignKey('study_area.id'), primary_key=True)
)


############################################################
#         student - university relationship                 =================================
############################################################
student_applicable_universities = db.Table(
    'student_applicable_universities',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('university_id', db.Integer, db.ForeignKey('university.id'))
)

student_assigned_university = db.Table(
    'student_assigned_university',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('university_id', db.Integer, db.ForeignKey('university.id'))
)


University.students = db.relationship('Student', secondary=student_applicable_universities, back_populates='applicable_universities')
Student.applicable_universities = db.relationship('University', secondary=student_applicable_universities, back_populates='students')

Student.assigned_university = db.relationship('University', secondary=student_assigned_university, back_populates='assigned_students', uselist=False)
University.assigned_students = db.relationship('Student', secondary=student_assigned_university, back_populates='assigned_university')

StudyArea.universities = db.relationship('University', secondary=university_study_area, back_populates='study_areas')
University.study_areas = db.relationship('StudyArea', secondary=university_study_area, back_populates='universities')

Student.study_areas = db.relationship('StudyArea', secondary=student_study_area, back_populates='students')
StudyArea.students = db.relationship('Student', secondary=student_study_area, back_populates='study_areas')

Language.study_areas = db.relationship('StudyArea', secondary=language_study_area, back_populates='language')
StudyArea.language = db.relationship('Language', secondary=language_study_area, back_populates='study_areas')

Language.students = db.relationship('Student', secondary=language_student, back_populates='languages')
Student.languages = db.relationship('Language', secondary=language_student, back_populates='students')
