
from flask import Flask, request, render_template, redirect, url_for
from service import app, db
from service.models.student import Student, StudyArea, Language, University, Accommodation


@app.route('/accommodations')
def list_accommodations():
    accommodations = Accommodation.query.all()
    return "not available yet"
    #return render_template('list_students.html', accommodations=accommodations)