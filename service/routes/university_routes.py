
from flask import Flask, request, render_template, redirect, url_for
from service import app, db
from service.models.student import University, StudyArea

@app.route('/universities/create', methods=['GET', 'POST'])
def create_university():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        id = University.query.count() + 1

        selected_study_areas = request.form.getlist('study_areas')
        study_areas = StudyArea.query.filter(StudyArea.id.in_(selected_study_areas)).all()

        university = University(name=name, location=location, study_areas=study_areas)
        db.session.add(university)
        db.session.commit()

        return redirect(url_for('list_universities'))
    
    study_areas = StudyArea.query.all()
    return render_template('create_university.html', study_areas=study_areas)


@app.route('/universities')
def list_universities():
    universities = University.query.all()

    universities_with_students = []
    for university in universities:
        students = university.assigned_students
        universities_with_students.append((university, students))

    return render_template('list_universities.html', universities=universities, universities_with_students=universities_with_students)


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
