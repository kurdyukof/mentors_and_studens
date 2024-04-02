class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_bl(self, lecturer, l_course, grade):
        if isinstance(lecturer,
                      Lecturer) and l_course in self.courses_attached and l_course in lecturer.l_courses_in_progress:
            if l_course in lecturer.grades:
                lecturer.grades[l_course] += [grade]
            else:
                lecturer.grades[l_course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.l_courses_attached = []
        self.courses_attached = []
        self.grades = {}
        self.lecturers = Lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.course = []

    def rate_nw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка!"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_nw(best_student, 'Python', 10)
cool_reviewer.rate_nw(best_student, 'Python', 10)
cool_reviewer.rate_nw(best_student, 'Python', 10)

best_lecturer = Lecturer('Chaki', 'Dools')
best_lecturer.l_courses_attached += ['Git']

student.rate_bl(best_lecturer, 'Git', 15)
cools_student.rate_bl(best_lecturer, 'Git', 15)
cools_student.rate_bl(best_lecturer, 'Git', 15)

print(best_student.grades)
print(best_lecturer.grades)
