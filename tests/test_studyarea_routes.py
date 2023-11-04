import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from service import app, db
from service.models.student import StudyArea

class TestCreateStudyAreaRoute(TestCase):
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

    def test_create_study_area_form(self):
        response = self.client.get('/study_area/create')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('create_study_area.html')

    def test_create_study_area(self):
        response = self.client.post('/study_area/create', data={'name': 'Science'})
        self.assertRedirects(response, '/study_areas')

        study_area = StudyArea.query.filter_by(name='Science').first()
        self.assertIsNotNone(study_area)


    def test_list_study_areas(self):
        study_area1 = StudyArea(name="Science")
        study_area2 = StudyArea(name="Math")
        db.session.add(study_area1)
        db.session.add(study_area2)
        db.session.commit()

        response = self.client.get('/study_areas')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('list_study_areas.html')

        self.assertContext('study_areas', [study_area1, study_area2])


    def test_edit_study_area(self):
        study_area = StudyArea(name="Science")
        db.session.add(study_area)
        db.session.commit()

        response = self.client.get(f'/study_areas/{study_area.id}/edit')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('edit_study_area.html')
        self.assertContext('study_area', study_area)

        response = self.client.post(f'/study_areas/{study_area.id}/edit', data={'name': 'Math'})
        self.assertEqual(response.status_code, 302)

        updated_study_area = StudyArea.query.get(study_area.id)
        self.assertEqual(updated_study_area.name, 'Math')

        response = self.client.get('/study_areas')
        self.assertIn(b'Math', response.data)


    def test_delete_study_area(self):
        study_area = StudyArea(name="Science")
        db.session.add(study_area)
        db.session.commit()

        response = self.client.post(f'/study_areas/{study_area.id}/delete')
        self.assertEqual(response.status_code, 302)

        deleted_study_area = StudyArea.query.get(study_area.id)
        self.assertIsNone(deleted_study_area)

        response = self.client.get('/study_areas')
        self.assertNotIn(b'Science', response.data)


if __name__ == '__main__':
    unittest.main()
