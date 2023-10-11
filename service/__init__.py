
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://asanguine:<PASSWORD>@asanguine.mysql.pythonanywhere-services.com/asanguine$default'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from service.models.student import Student, University, Accommodation, StudyArea

from service.routes import *


# Ensure the database tables are created
with app.app_context():
    db.create_all()




@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
