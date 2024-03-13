class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_hw(self, best_student, param, param1):
        pass


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.corses_attached = []
        self.lecturer = Lecturer
        self.grades = {}
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviewer = reviewer
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []

        def rate_hw(self, lecturer, course, grade):
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Student('Some', 'Buddy','your_gender')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Semen', 'Semenov')
best_lecturer.courses_attached += ['Python']

cool_student = Lecturer('Ivan', 'Ivanov')
cool_student.corses_attached += ['Git']

cool_student.rate_hw(best_lecturer, 'Git', 10)
cool_student.rate_hw(best_lecturer, 'Git', 10)
cool_student.rate_hw(best_lecturer, 'Git', 10)

print(best_student.grades)
print(best_lecturer.grades)