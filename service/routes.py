
# from flask import Flask, request, render_template, redirect, url_for
# from . import app, db

# from service.models.student import Student
# from service.models.university import University
# from service.models.accommodation import Accommodation
# from service.models.studyArea import StudyArea

# ############################################################
# #                       Routes
# ############################################################


# @app.route('/')
# def home():
#     students = Student.query.all()
#     return redirect(url_for('list_students'))

# @app.route('/students/create', methods=['GET', 'POST'])
# def create_student():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         major = request.form.get('major')
#         budget = request.form.get('budget')
#         email = request.form.get('email')
#         phone_number = request.form.get('phone_number')
#         id = Student.query.count() + 1

#         student = Student(name=name, major=major, budget=budget)
#         db.session.add(student)
#         db.session.commit()

#         return redirect(url_for('list_students'))
    
#     return render_template('create_student.html')


# @app.route('/students')
# def list_students():
#     students = Student.query.all()
#     return render_template('list_students.html', students=students)


# @app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
# def edit_student(id):
#     student = Student.query.get(id)

#     if request.method == 'POST':
#         student.name = request.form.get('name')
#         student.major = request.form.get('major')
#         student.income = request.form.get('income')

#         db.session.commit()
#         return redirect(url_for('list_students'))

#     return render_template('edit_student.html', student=student)


# @app.route('/students/<int:id>/delete', methods=['POST'])
# def delete_student(id):
#     student = Student.query.get(id)

#     db.session.delete(student)
#     db.session.commit()

#     return redirect(url_for('list_students'))
