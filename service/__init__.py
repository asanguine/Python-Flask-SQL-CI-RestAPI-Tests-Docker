"""
Data Models
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://asanguine:15975acfKjfydJ18SQL@asanguine.mysql.pythonanywhere-services.com/asanguine$default'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

#from service.models import Student, University, Accommodation, StudyArea
from service.models.student import Student
from service.models.university import University
from service.models.accommodation import Accommodation
from service.models.studyArea import StudyArea

from service import routes


# Ensure the database tables are created
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return 'Welcome to the Student Counseling Service!'




if __name__ == '__main__':
    app.run(debug=True)
