
def parse_grades(grades_raw):
    grade_data = {}

    for item in grades_raw.split():
        student = item.split(":")[0]
        course = item.split(":")[1]
        marks= item.split(":")[2]
        marks = int(marks)

        if student not in grade_data:
            grade_data[student] = {}

        grade_data[student][course] = marks

    return grade_data



def get_course_credits(courses_raw):
    return {c[0]: c[3] for c in courses_raw}



def grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 75:
        return 8
    elif marks >= 60:
        return 6
    elif marks >= 50:
        return 4
    else:
        return 0


def calculate_gpa(student, grade_data, course_credits):
    total_points = 0
    total_credits = 0

    for course, marks in grade_data[student].items():
        gp = grade_point(marks)
        credits = course_credits[course]

        total_points += gp * credits
        total_credits += credits

    return round(total_points / total_credits, 2)



def class_report(grade_data):
    report = []

    courses = set()
    for student in grade_data:
        courses.update(grade_data[student].keys())

    for course in courses:
        total = 0
        count = 0
        top_student = ""
        top_marks = 0

        for student in grade_data:
            if course in grade_data[student]:
                marks = grade_data[student][course]

                total += marks
                count += 1

                if marks > top_marks:
                    top_marks = marks
                    top_student = student

        avg = total / count
        report.append((course, round(avg, 2), top_student))

    report.sort(key=lambda x: x[1], reverse=True)

    return report

grades_raw="alice:CS101:88 alice:CS201:76 alice:EN101:92 bob:CS101:65 charlie:CS201:55 charlie:MA101:48 charlie:EN101:71"
courses_raw = [
("CS101","Intro to Python", "Mon 09:00", 3, "Dr. Rao"),
("CS201","Data Structures", "Wed 10:00", 4, "Dr. Meera"),
("MA101","Calculus", "Mon 09:00", 3, "Dr. Suresh"),
("EN101","English Writing", "Fri 11:00", 2, "Dr. Priya"),
]

grade_data = parse_grades(grades_raw)
course_credits = get_course_credits(courses_raw)

print("Grade Data:", grade_data)

print("\nGPA:")
for student in grade_data:
    print(student, "→", calculate_gpa(student, grade_data, course_credits))

print("\nClass Report:")
for r in class_report(grade_data):
    print(r)
