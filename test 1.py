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



    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
            average_rating = round(sum_rating / len_rating, 2)
         return average_rating


    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
           if lesson == course:
            sum_rating += sum(self.grades[course])
            len_rating += len(self.grades[course])
            average_rating = round(sum_rating / len_rating, 2)
         return average_rating


    def __str__(self):
      res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
      return res


    def __lt__(self, other):
      if not isinstance(other, Student):
        print("Преподователей и студентов между собой не сравнивают!")
        return self.av_rating() < other.av_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.l_gradescourses_attached = []
        self.l_courses = []
        self.l_courses_attached = []
        self.l_grades = {}
        self.lecturers = Lecturer
        self.l_courses_in_progress = []

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


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

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating

print(some_student)
print(best_student.grades)
print(best_lecturer.l_grades)
print(some_reviewer)
print(some_lecturer)
