import unittest
from flask import Flask
from flask_testing import TestCase
from service import app, db
from service.models.student import University, StudyArea

class TestUniversityRoutes(TestCase):
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


    def test_create_university_form(self):
        response = self.client.get('/universities/create')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('create_university.html')


    def test_edit_university_form(self):
        university = University(name="Sample University", location="Sample Location")
        db.session.add(university)
        db.session.commit()

        response = self.client.get(f'/universities/{university.id}/edit')

        self.assertEqual(response.status_code, 200)
        self.assert_template_used('edit_university.html')

        self.assert_context('university', university)


    def test_create_university(self):
        study_area = StudyArea(name='Science')
        db.session.add(study_area)
        db.session.commit()

        response = self.client.post('/universities/create', data=dict(
            name='Test University',
            location='Test Location',
            study_areas=['1']
        ))

        self.assertRedirects(response, 'http://localhost/list_universities')

        university = University.query.first()
        self.assertIsNotNone(university)
        self.assertEqual(university.name, 'Test University')
        self.assertEqual(university.location, 'Test Location')
        self.assertIn(study_area, university.study_areas)


    def test_list_universities(self):
        university = University(name="Uni1", location="Location1")
        db.session.add(university)
        db.session.commit()

        response = self.client.get('/universities')
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Uni1', response.data)


    def test_edit_university(self):
        university = University(name="Uni1", location="Location1")
        db.session.add(university)
        db.session.commit()

        response = self.client.post(f'/universities/{university.id}/edit', data=dict(
            name='UpdatedUni',
            location='UpdatedLocation'
        ))
        self.assertEqual(response.status_code, 302)

        updated_university = University.query.get(university.id)
        self.assertEqual(updated_university.name, 'UpdatedUni')
        self.assertEqual(updated_university.location, 'UpdatedLocation')


    def test_delete_university(self):
        university = University(name="Uni1", location="Location1")
        db.session.add(university)
        db.session.commit()

        response = self.client.post(f'/universities/{university.id}/delete')
        self.assertEqual(response.status_code, 302)

        deleted_university = University.query.get(university.id)
        self.assertIsNone(deleted_university)


if __name__ == '__main__':
    unittest.main()
