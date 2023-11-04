import unittest
from flask import Flask
from flask_testing import TestCase
from service import app, db
from service.models.student import Accommodation

class TestAccommodationsRoute(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



    def test_list_accommodations(self):
        response = self.client.get('/accommodations')

        self.assert200(response)
if __name__ == '__main__':
    unittest.main()
