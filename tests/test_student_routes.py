import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from service import app, db
from service.models.student import Student, StudyArea, Language, University
from service.routes import student_routes
from service.matching.university_matching import match_students_to_universities

class TestCreateStudentRoute(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    

    # def test_create_student(self):
    #     Language.create_hardcoded_languages()
    #     study_area1 = StudyArea("Science")
    #     study_area2 = StudyArea("Math")
    #     study_area_for_uni = StudyArea("Science - English")
    #     university = University(name="Uni1", location="loc1")
    #     university.study_areas.append(study_area_for_uni)

    #     db.session.add(study_area1)
    #     db.session.add(study_area2)
    #     db.session.add(study_area_for_uni)
    #     db.session.add(university)
    #     db.session.commit()

    #     response = self.client.post('/students/create', data=dict(
    #         name='John Doe',
    #         budget=10000,
    #         email='john@example.com',
    #         phone_number='1234567890',
    #         study_areas=['1'],
    #         languages=['1']
    #     ))

    #     self.assertRedirects(response, '/students')

    #     student = Student.query.first()
    #     self.assertIsNotNone(student)
    #     self.assertEqual(student.name, 'John Doe')


if __name__ == '__main__':
    unittest.main()
