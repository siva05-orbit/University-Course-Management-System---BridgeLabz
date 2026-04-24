from itertools import combinations

class Course:
    def __init__(self, code, name, timeslot, credits, instructor):
        self.code = code
        self.name = name
        self.timeslot = timeslot
        self.credits = credits
        self.instructor = instructor
    
    def build_timeslot_map(courses):
        timeslot_map = {}
        for c in courses:
            timeslot_map.setdefault(c.timeslot, []).append(c.code)
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




def main():
    courses_raw = [
    ("CS101","Intro to Python", "Mon 09:00", 3, "Dr. Rao"),
    ("CS201","Data Structures", "Wed 10:00", 4, "Dr. Meera"),
    ("MA101","Calculus", "Mon 09:00", 3, "Dr. Suresh"), # conflicts!
    ("EN101","English Writing", "Fri 11:00", 2, "Dr. Priya"),
    ]
    enrollments = {
    "alice": ["CS101","CS201","EN101"],
    "bob": ["CS101","MA101"], # schedule conflict
    "charlie": ["CS201","MA101","EN101"],
    }
    grades_raw = "alice:CS101:88 alice:CS201:76 alice:EN101:92 bob:CS101:65 charlie:CS201:55 charlie:MA101:48 charlie:EN101:71"

    
    courses = [Course(*c) for c in courses_raw]

    course_dict = {c.code: c for c in courses}

    timeslot_map = Course.build_timeslot_map(courses)
   
    conflict_report = Course.detect_conflicts(enrollments, course_dict)

    conflict_free = Course.get_conflict_free(conflict_report)

    print("timeslot_map =", timeslot_map)
    print("conflict_report =", conflict_report)
    print("conflict_free =", conflict_free)


main()