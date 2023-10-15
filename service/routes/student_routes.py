
from flask import Flask, request, render_template, redirect, url_for
from service import app, db
from service.models.student import Student, StudyArea, Language, University
from service.matching.university_matching import match_students_to_universities

@app.route('/students/create', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        name = request.form.get('name')
        budget = request.form.get('budget')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        id = Student.query.count() + 1

        selected_study_areas = request.form.getlist('study_areas')  # Get selected study areas from the form
        study_areas = StudyArea.query.filter(StudyArea.id.in_(selected_study_areas)).all()

        selected_languages = request.form.getlist('languages')
        languages = Language.query.filter(Language.id.in_(selected_languages)).all()

        student = Student(name=name, email=email, phone_number=phone_number, budget=budget, study_areas=study_areas, languages=languages)
        db.session.add(student)

        match_students_to_universities()
        db.session.commit()
        return redirect(url_for('list_students'))
    
    languages = Language.query.all()
    study_areas = StudyArea.query.all()    
    return render_template('create_student.html', study_areas=study_areas, languages=languages)


@app.route('/students')
def list_students():
    students = Student.query.all()
    return render_template('list_students.html', students=students)


@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get(id)
    all_study_areas = StudyArea.query.all()
    all_languages = Language.query.all()

    if request.method == 'POST':
        student.name = request.form.get('name')
        student.major = request.form.get('major')
        student.budget = request.form.get('budget')
        student.email = request.form.get('email')
        student.phone_number = request.form.get('phone_number')

        selected_study_areas = request.form.getlist('study_areas')
        study_areas = StudyArea.query.filter(StudyArea.id.in_(selected_study_areas)).all()
        student.study_areas = study_areas

        selected_languages = request.form.getlist('languages')
        languages = Language.query.filter(Language.id.in_(selected_languages)).all()
        student.languages = languages

        match_students_to_universities()
        db.session.commit()
        return redirect(url_for('list_students'))
    
    return render_template('edit_student.html', student=student, all_study_areas=all_study_areas, all_languages=all_languages)


@app.route('/students/<int:id>/delete', methods=['POST'])
def delete_student(id):
    student = Student.query.get(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for('list_students'))