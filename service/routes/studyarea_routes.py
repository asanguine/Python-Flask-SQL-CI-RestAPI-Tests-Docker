
from flask import Flask, request, render_template, redirect, url_for
from service import app, db
from service.models.student import StudyArea

@app.route('/study_area/create', methods=['GET', 'POST'])
def create_study_area():
    if request.method == 'POST':
        name = request.form.get('name')
        id = StudyArea.query.count() + 1

        study_area = StudyArea(name=name)
        db.session.add(study_area)
        db.session.commit()

        return redirect(url_for('list_study_areas'))
    
    return render_template('create_study_area.html')


@app.route('/study_areas')
def list_study_areas():
    study_areas = StudyArea.query.all()
    return render_template('list_study_areas.html', study_areas=study_areas)


@app.route('/study_areas/<int:id>/edit', methods=['GET', 'POST'])
def edit_study_area(id):
    study_area = StudyArea.query.get(id)

    if request.method == 'POST':
        study_area.name = request.form.get('name')

        db.session.commit()
        return redirect(url_for('list_study_areas'))

    return render_template('edit_study_area.html', study_area=study_area)


@app.route('/study_areas/<int:id>/delete', methods=['POST'])
def delete_study_area(id):
    study_area = StudyArea.query.get(id)

    db.session.delete(study_area)
    db.session.commit()

    return redirect(url_for('list_study_areas'))