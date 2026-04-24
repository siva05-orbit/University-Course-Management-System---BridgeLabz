from itertools import combinations
# MEMBER 1
class Course:
    def __init__(self, course_code, course_name, timeslot, credits, professor):
        self.course_code = course_code
        self.course_name = course_name
        self.timeslot = timeslot
        self.credits = credits
        self.professor = professor

    def __str__(self):
        return f"{self.course_code} | {self.course_name} | {self.timeslot} | {self.credits} credits | {self.professor}"


class GradedStudent:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.courses = []
        self.credits = 0

    def enroll(self, course):
        self.courses.append(course)
        self.credits += course.credits

    def __len__(self):
        return len(self.courses)


# MEMBER 2
class CourseHelper:

    def build_timeslot_map(courses):
        timeslot_map = {}
        for c in courses:
            timeslot_map.setdefault(c.timeslot, []).append(c.course_code)
        return timeslot_map

    def detect_conflicts(enrollments, course_dict):
        conflict_report = {}

        for student, course_codes in enrollments.items():

            slot_map = {}
            for code in course_codes:
                slot = course_dict[code].timeslot
                slot_map.setdefault(slot, []).append(code)

            conflicts = []

            for slot, codes in slot_map.items():
                if len(codes) > 1:
                    for c1, c2 in combinations(codes, 2):
                        conflicts.append((c1, c2, slot))

            conflict_report[student] = conflicts

        return conflict_report

    def get_conflict_free(conflict_report):
        return {student for student, conflicts in conflict_report.items() if not conflicts}


# MEMBER 3

def parse_grades(grades_raw):
    grade_data = {}

    for item in grades_raw.split():
        student = item.split(":")[0]
        course = item.split(":")[1]
        marks = item.split(":")[2]
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
        top_marks = -1

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



if __name__ == "__main__":

    # INPUT 
    courses_raw = [
        ("CS101","Intro to Python", "Mon 09:00", 3, "Dr. Rao"),
        ("CS201","Data Structures", "Wed 10:00", 4, "Dr. Meera"),
        ("MA101","Calculus", "Mon 09:00", 3, "Dr. Suresh"),
        ("EN101","English Writing", "Fri 11:00", 2, "Dr. Priya"),
    ]

    enrollments = {
        "alice": ["CS101","CS201","EN101"],
        "bob": ["CS101","MA101"],
        "charlie": ["CS201","MA101","EN101"],
    }

    grades_raw = "alice:CS101:88 alice:CS201:76 alice:EN101:92 bob:CS101:65 charlie:CS201:55 charlie:MA101:48 charlie:EN101:71"


    print("\n--- MEMBER 1 OUTPUT ---")

    courses = [Course(*c) for c in courses_raw]

    c = courses[0]
    print(str(c))

    s = GradedStudent("Alice", 1)
    s.enroll(c)

    print("Courses Enrolled:", len(s))
    print("Total Credits:", s.credits)



    print("\n--- MEMBER 2 OUTPUT ---")

    course_dict = {c.course_code: c for c in courses}

    timeslot_map = CourseHelper.build_timeslot_map(courses)
    conflict_report = CourseHelper.detect_conflicts(enrollments, course_dict)
    conflict_free = CourseHelper.get_conflict_free(conflict_report)

    print("timeslot_map =", timeslot_map)
    print("conflict_report =", conflict_report)
    print("conflict_free =", conflict_free)



    print("\n--- MEMBER 3 OUTPUT ---")

    grade_data = parse_grades(grades_raw)
    course_credits = get_course_credits(courses_raw)

    print("\nGPA:")
    for student in grade_data:
        print(student, "→", calculate_gpa(student, grade_data, course_credits))

    print("\nClass Report:")
    for r in class_report(grade_data):
        print(r)