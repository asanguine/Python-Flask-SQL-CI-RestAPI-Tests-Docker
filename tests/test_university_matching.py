import unittest
from flask import Flask
from service import app, db
from service.models.student import Student, University, StudyArea, Language
from service.matching.university_matching import match_students_to_universities

class TestUniversityMatching(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()


############################################################
#                    TEST CASES
############################################################


    def test_match_students_to_universities(self):
        with app.app_context():
            study_area = StudyArea(name="Science")
            study_area_of_uni = StudyArea(name="Science - English")
            db.session.add(study_area)
            db.session.add(study_area_of_uni)
            db.session.commit()

            language = Language(name="English")
            db.session.add(language)
            db.session.commit()

            university = University(name="uni",
                                    location="Sample Location",
                                    study_areas=[study_area_of_uni])
            db.session.add(university)
            db.session.commit()

            student = Student(name='Birkan',
                budget=10000,
                email='birkan@example.com',
                phone_number='1234567890',
                study_areas=[study_area],
                languages=[language])
            
            student.assigned_university = university
            db.session.add(student)
            db.session.commit()

            match_students_to_universities()

            student = Student.query.first()
            self.assertEqual(len(student.applicable_universities), 1)
            self.assertEqual(student.applicable_universities[0].name, "uni")

if __name__ == '__main__':
    unittest.main()
