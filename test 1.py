class Student:
    def __init__(self, name, surname):
        self.l_courses_attached = []
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_bl(self, lecturer, l_course, l_grade, ):
        if isinstance(lecturer,
                      Lecturer) and l_course in self.l_courses_attached and l_course in lecturer.courses_in_progress:
            if l_course in lecturer.l_grades:
                lecturer.l_grades[l_course] += [l_grade]
            else:
                lecturer.l_grades[l_course] = [l_grade]
        else:
            return 'Ошибка'

    def medium_grade_student(self):
        list_grade = self.grades.values()
        sum_grade = 0
        for grade_student in list_grade:
            sum_grade += sum(grade_student)
            return sum_grade / len(grade_student)

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}\nКурсы "
                f"в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return self.medium_grade_student() < other_student.medium_grade_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.l_gradescourses_attached = []
        self.l_courses = []
        self.l_courses_attached = []
        self.l_grades = {}
        self.lecturers = Lecturer
        self.l_courses_in_progress = []

    def medium_grade(self):
        list_grade = self.l_grades.values()
        sum_grade = 0
        for grade_lecturer in list_grade:
            sum_grade += sum(grade_lecturer)
            return sum_grade / len(grade_lecturer)

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self.medium_grade() < other_lecturer.medium_grade()

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.l_grades}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_nw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка!"

    def __str__(self):
        return f"Имя:{self.name},\nФамилия: {self.surname}"


student_1 = Student('Юлия', 'Топова')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Design']
student_2 = Student('Василий', 'Кокорин')
student_2.courses_in_progress += ['Design']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Анатолий', 'Тюрин')
lecturer_1.l_courses_attached += ['Python']
lecturer_2 = Lecturer('Антонина', 'Моисеенко')
lecturer_2.l_gradescourses_attached += ['Design']

student_1.rate_bl(lecturer_1, 'Python', 10)
student_2.rate_bl(lecturer_2, 'Design', 8)

reviewer_1 = Reviewer('Анна', 'Хорина')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Иван', 'Просеков')
reviewer_2.courses_attached += ['Design']

reviewer_1.rate_nw(student_1, 'Python', 9)
reviewer_2.rate_nw(student_2, 'Design', 7)
best_student = Student('Ruoy', 'Eman')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_nw(best_student, 'Python', 10)
cool_reviewer.rate_nw(best_student, 'Python', 10)
cool_reviewer.rate_nw(best_student, 'Python', 10)

best_lecturer = Lecturer('Дмитрий ', 'Макаров')
best_lecturer.l_courses_attached += ['Git']

cool_student = Student('Андрей', 'Поляков')

cool_student.rate_bl(best_lecturer, 'Git', 15)
cool_student.rate_bl(best_lecturer, 'Git', 15)
cool_student.rate_bl(best_lecturer, 'Git', 15)

some_reviewer = Reviewer('Some', 'Boddy')
some_lecturer = Lecturer('Some', 'Boddy')
some_student = Student('Ruoy', 'Eman')

print(some_student)
print(best_student.grades)
print(best_lecturer.l_grades)
print(some_reviewer)
print(some_lecturer)
