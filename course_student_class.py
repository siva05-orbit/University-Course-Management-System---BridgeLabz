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


# Backward-compatible aliases for the original lowercase class names.
course = Course
student = GradedStudent


if __name__ == "__main__":
    c = Course("CS101", "Intro to Python", "Mon 09:00", 3, "Dr. Rao")
    print(str(c))

    s = GradedStudent("Alice", roll=1)
    s.enroll(c)
    print(len(s))
    print(s.credits)