
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############################################################
#                   Accommodation Model
############################################################
class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # Example: Hotel, Dormitory, etc.
    price = db.Column(db.Integer)
    location = db.Column(db.String(100))

PREDEFINED_ACCOMMODATION_TYPES = [
    'Hotel',
    'Airbnb',
    'Private Dorm',
    'School Dorm',
    'Apartment',
]