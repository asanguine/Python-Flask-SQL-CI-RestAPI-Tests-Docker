from collections import defaultdict
from service.models.student import Student, University

def match_students_to_universities():
    students = Student.query.all()
    universities = University.query.all()

    for student in students:
        student.applicable_universities = []
        print(f"Student: {student.name}, Study Areas: {[sa.name for sa in student.study_areas]}, Languages: {[lang.name for lang in student.languages]}")
        for preferred_study_area in student.study_areas:
            for university in universities:
                # Scoring System
                score = 0

                for language in student.languages:
                    print(f"language: {language.name}")
                    for study_area in university.study_areas:
                        print(f"uni's study area: {study_area.name}")
                        print(f"students's study area: {preferred_study_area.name}")
                        if preferred_study_area.name in study_area.name and language.name in study_area.name:
                            score += 1
                print(f"score: {score}") 

                # Ranking Universities
                if score > 0 and student not in university.students:
                    student.applicable_universities.append((university))
                    
        #print(f"Applicable Universities: {[app_uni.name for app_uni in student.applicable_universities]}")
        # Assign Universities to Students
        #student.applicable_universities.sort(key=lambda x: x[1], reverse=True)



# # Step 6: Record Assigned University (Example: Assign the top match)
# for student in students:
#     if student.applicable_universities:
#         student.assigned_university = student.applicable_universities[0][0].name
