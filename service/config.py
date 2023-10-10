"""
Global Configuration for Application
"""
import os

class Config:

    # Get configuration from environment
    #DATABASE_URI = os.getenv("DATABASE_URI")


    # Configure SQLAlchemy
    #SQLALCHEMY_DATABASE_URI = DATABASE_URI
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_DATABASE_URI = 'mysql://asanguine:15975acfKjfydJ18SQL@asanguine.mysql.pythonanywhere-services.com/asanguine$default'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret for session management
    SECRET_KEY = os.getenv("SECRET_KEY", "s3cr3t-key-shhhh")