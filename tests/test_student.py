
import unittest
from factory import Factory, SubFactory
from nose.tools import eq_, ok_
from service import db, app  # Import your app and database
from service.models.student import Student, StudyArea, University, Language, DataValidationError  # Import your Student model
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

############################################################
#                    TEST CASES
############################################################
        
    def test_student_repr(self):
        student = Student(name="John")
        expected_repr = '<Student \'John\'>'
        self.assertEqual(repr(student), expected_repr)


    def test_to_dict(self):
        student = StudentFactory()
        student_dict = student.to_dict()

        expected_dict = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'phone_number': student.phone_number,
            'budget': student.budget,
            'status': student.status
        }
        self.assertDictEqual(student_dict, expected_dict)


    def test_from_dict(self):
        student = StudentFactory.build()
        
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '123-456-7890',
            'budget': 5000,
            'status': 'Active'
        }
        
        student.from_dict(data)
        
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.email, 'john@example.com')
        self.assertEqual(student.phone_number, '123-456-7890')
        self.assertEqual(student.budget, 5000)
        self.assertEqual(student.status, 'Active')


    def test_create(self):
        student = StudentFactory.build()
        student.create()
        self.assertIn(student, db.session)


    def test_update(self):
        student = StudentFactory.create()
        student.update()


    def test_delete(self):
        #student = StudentFactory.create()
        student = StudentFactory.build()
        student.create()
        student.delete()
        deleted_student = Student.query.get(student.id)
        self.assertIsNone(deleted_student)


    def test_study_area_init(self):
        study_area = StudyArea("Science")
        self.assertEqual(study_area.name, "Science")

    
    def test_language_init(self):
        language = Language("English")
        self.assertEqual(language.name, "English")


    def test_university_repr(self):
        university = University(name="Uni1")
        expected_repr = '<University Uni1>'
        self.assertEqual(repr(university), expected_repr)


    def test_student_update_empty_id(self):
        student = Student(name="John Doe")
        with self.assertRaises(DataValidationError):
            student.update()


    def test_create_hardcoded_languages(self):
        initial_languages = Language.query.all()
        self.assertEqual(len(initial_languages), 0)

        Language.create_hardcoded_languages()

        english = Language.query.filter_by(name='English').first()
        german = Language.query.filter_by(name='German').first()

        self.assertIsNotNone(english)
        self.assertIsNotNone(german)


if __name__ == '__main__':
    import nose
    nose.main()
