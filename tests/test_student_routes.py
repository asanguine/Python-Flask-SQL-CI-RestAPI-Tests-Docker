import unittest
from flask import Flask
from flask_testing import TestCase
from service import app, db
from service.models.student import University, StudyArea, Student, Language

class TestStudentRoutes(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

############################################################
#                    TEST CASES
############################################################


    def test_create_student_form(self):
        response = self.client.get('/students/create')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('create_student.html')


    def test_edit_student_form(self):
        study_area1 = StudyArea(name="studyarea1")
        study_area2 = StudyArea(name="studyarea2")
        db.session.add(study_area1)
        db.session.add(study_area2)
        db.session.commit()

        language1 = Language(name="English")
        language2 = Language(name="German")
        db.session.add(language1)
        db.session.add(language2)
        db.session.commit()

        university1 = University(name="University1", location="Sample Location")
        university2 = University(name="University2", location="Sample Location")
        db.session.add(university1)
        db.session.add(university2)
        db.session.commit()

        response = self.client.post('/students/create', data=dict(
            name='Birkan',
            budget=10000,
            email='birkan@example.com',
            phone_number='1234567890',
            study_areas=['1'],
            languages=['1']
        ))
        student = Student.query.first()
        student.assigned_university = university1
        db.session.add(student)
        db.session.commit()

        response = self.client.get(f'/students/{student.id}/edit')

        self.assertEqual(response.status_code, 200)
        self.assert_template_used('edit_student.html')

        self.assert_context('student', student)


    def test_create_student(self):
        study_area = StudyArea(name="Sample Study Area")
        db.session.add(study_area)
        db.session.commit()

        university = University(name="Sample University", location="Sample Location")
        db.session.add(university)
        db.session.commit()

        response = self.client.post('/students/create', data=dict(
            name='Birkan',
            budget=10000,
            email='birkan@example.com',
            phone_number='1234567890',
            study_areas=['1'],
            languages=['1']
        ))

        self.assertRedirects(response, 'http://localhost/list_students')

        student = Student.query.first()
        self.assertIsNotNone(student)
        self.assertEqual(student.name, 'Birkan')


    def test_list_students(self):
        response = self.client.get('/students')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('list_students.html')


    def test_edit_student(self):
        study_area1 = StudyArea(name="studyarea1")
        study_area2 = StudyArea(name="studyarea2")
        db.session.add(study_area1)
        db.session.add(study_area2)
        db.session.commit()

        language1 = Language(name="English")
        language2 = Language(name="German")
        db.session.add(language1)
        db.session.add(language2)
        db.session.commit()

        university1 = University(name="University1", location="Sample Location")
        university2 = University(name="University2", location="Sample Location")
        db.session.add(university1)
        db.session.add(university2)
        db.session.commit()

        response = self.client.post('/students/create', data=dict(
            name='Birkan',
            budget=10000,
            email='birkan@example.com',
            phone_number='1234567890',
            study_areas=['1'],
            languages=['1']
        ))
        student = Student.query.first()
        student.assigned_university = university1
        db.session.add(student)
        db.session.commit()

        response = self.client.post(f'/students/{student.id}/edit', data=dict(
            name='John Updated',
            budget=20000,
            email='john.updated@example.com',
            phone_number=9876543210,
            study_areas=['2'],
            languages=['2'],
            assigned_university_id=university2.id
        ))

        self.assertRedirects(response, 'http://localhost/list_students')

        updated_student = Student.query.get(student.id)
        self.assertIsNotNone(updated_student)
        self.assertEqual(updated_student.name, 'John Updated')
        self.assertEqual(updated_student.budget, 20000)
        self.assertEqual(updated_student.email, 'john.updated@example.com')
        self.assertEqual(updated_student.phone_number, 9876543210)
        self.assertIsNotNone(updated_student.assigned_university)
        #self.assertIsNone(updated_student.assigned_university)
        self.assertEqual(updated_student.assigned_university.id, university2.id)

        # self.assert_template_used('edit_student.html')
        # self.assertIsNotNone(response.context['all_study_areas'])
        # self.assertIsNotNone(response.context['all_languages'])
        # self.assertIsNotNone(response.context['all_universities'])


    def test_delete_student(self):
        student = Student(name="Birkan")
        db.session.add(student)
        db.session.commit()

        response = self.client.post(f'/students/{student.id}/delete')
        self.assertRedirects(response, 'http://localhost/list_students')
        deleted_student = Student.query.get(student.id)
        self.assertIsNone(deleted_student)


if __name__ == '__main__':
    unittest.main()
