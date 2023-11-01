# """
# Test Cases TestAccountModel
# """

# from unittest import TestCase
# from service import db
# from service.models import Student, DataValidationError
# from factories import StudentFactory


# class TestAccountModel(TestCase):
#     """Test Account Model"""

#     @classmethod
#     def setUpClass(cls):
#         """ Load data needed by tests """
#         db.create_all()  # make our sqlalchemy tables

#     @classmethod
#     def tearDownClass(cls):
#         """Disconnext from database"""
#         db.session.close()

#     def setUp(self):
#         """Truncate the tables"""
#         db.session.query(Student).delete()
#         db.session.commit()

#     def tearDown(self):
#         """Remove the session"""
#         db.session.remove()

#     ######################################################################
#     #  T E S T   C A S E S
#     ######################################################################

#     def test_create_all_students(self):
#         """ Test creating multiple Accounts """
#         for _ in range(3):
#             student = StudentFactory()
#             student.create()
#         self.assertEqual(len(Student.all()), 3)

#     # def test_create_an_student(self):
#     #     """ Test Account creation using known data """
#     #     student = StudentFactory()
#     #     student.create()
#     #     self.assertEqual(len(Student.all()), 1)

#     # def test_repr(self):
#     #     """Test the representation of an student"""
#     #     student = Student()
#     #     student.name = "Foo"
#     #     self.assertEqual(str(student), "<Account 'Foo'>")

#     # def test_to_dict(self):
#     #     """ Test student to dict """
#     #     student = StudentFactory()
#     #     result = student.to_dict()
#     #     self.assertEqual(student.name, result["name"])
#     #     self.assertEqual(student.email, result["email"])
#     #     self.assertEqual(student.phone_number, result["phone_number"])
#     #     self.assertEqual(student.disabled, result["disabled"])
#     #     self.assertEqual(student.date_joined, result["date_joined"])

#     # def test_from_dict(self):
#     #     """ Test student from dict """
#     #     data = StudentFactory().to_dict()
#     #     student = Student()
#     #     student.from_dict(data)
#     #     self.assertEqual(student.name, data["name"])
#     #     self.assertEqual(student.email, data["email"])
#     #     self.assertEqual(student.phone_number, data["phone_number"])
#     #     self.assertEqual(student.disabled, data["disabled"])

#     # def test_update_an_student(self):
#     #     """ Test Account update using known data """
#     #     student = StudentFactory()
#     #     student.create()
#     #     self.assertIsNotNone(student.id)
#     #     student.name = "Rumpelstiltskin"
#     #     student.update()
#     #     found = Student.find(student.id)
#     #     self.assertEqual(found.name, student.name)

#     # def test_invalid_id_on_update(self):
#     #     """ Test invalid ID update """
#     #     student = StudentFactory()
#     #     student.id = None
#     #     self.assertRaises(DataValidationError, student.update)

#     # def test_delete_an_student(self):
#     #     """ Test Account update using known data """
#     #     student = StudentFactory()
#     #     student.create()
#     #     self.assertEqual(len(Student.all()), 1)
#     #     student.delete()
#     #     self.assertEqual(len(Student.all()), 0)


import unittest
from factory import Factory, SubFactory
from nose.tools import eq_, ok_
from service import db, app  # Import your app and database
from service.models.student import Student  # Import your Student model
from .factories import StudentFactory  # Import your StudentFactory

# Initialize your Factory with SQLAlchemy and your app
#Factory.set_session(db.session)

class TestStudentModel(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.ctx.pop()


        
    def test_student_repr(self):
        student = Student(name="John")
        expected_repr = '<Student \'John\'>'
        self.assertEqual(repr(student), expected_repr)


    # def test_student_creation(self):
    #     student = StudentFactory()
    #     db.session.add(student)
    #     db.session.commit()
    #     retrieved_student = Student.query.get(student.id)

    #     eq_(retrieved_student.name, student.name)
    #     eq_(retrieved_student.email, student.email)
    #     eq_(retrieved_student.phone_number, student.phone_number)
    #     eq_(retrieved_student.budget, student.budget)




if __name__ == '__main__':
    import nose
    nose.main()
