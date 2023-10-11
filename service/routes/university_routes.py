
from flask import Flask, request, render_template, redirect, url_for
from service import app, db
from service.models.student import University

@app.route('/universities/create', methods=['GET', 'POST'])
def create_university():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        id = University.query.count() + 1

        university = University(name=name, location=location)
        db.session.add(university)
        db.session.commit()

        return redirect(url_for('list_universities'))
    
    return render_template('create_university.html')


@app.route('/universities')
def list_universities():
    universities = University.query.all()
    return render_template('list_universities.html', universities=universities)


@app.route('/universities/<int:id>/edit', methods=['GET', 'POST'])
def edit_university(id):
    university = University.query.get(id)

    if request.method == 'POST':
        university.name = request.form.get('name')
        university.location = request.form.get('location')
        db.session.commit()
        return redirect(url_for('list_universities'))

    return render_template('edit_university.html', university=university)


@app.route('/universities/<int:id>/delete', methods=['POST'])
def delete_university(id):
    university = University.query.get(id)

    db.session.delete(university)
    db.session.commit()

    return redirect(url_for('list_universities'))