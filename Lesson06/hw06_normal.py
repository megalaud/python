
__author__ = 'Salyakhutdinov Rustem'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе



class Person:
    def __init__(self, surname, name, midname):
        self.surname = surname
        self.name = name
        self.midname = midname
        
    def fullname(self):
        return '{} {} {}'.format(self.surname, self.name, self.midname)

    def shortname(self):
        return '{} {}.{}.'.format(self.surname, self.name[0], self.midname[0])


class Student(Person):
    def __init__(self, surname, name, midname, father, mother, school_class):
        super().__init__(surname, name, midname)
        self.father = father
        self.mother = mother
        self.school_class = school_class

    def get_parents(self):
        return self.father.fullname(), self.mother.fullname()

class Teacher(Person):
    def __init__(self, surname, name, midname, school_subject):
        super().__init__(surname, name, midname)
        self.school_subject = school_subject

class School_class:
    def __init__(self, name):
        self.name = name
        self.school_subjects = []

    def subjectlist(self):
        return [s.school_subject for s in self.school_subjects]

    def teacherslist(self):
        return [s.shortname() for s in self.school_subjects]

class School:
    def __init__(self):
        self.classes = []
        self.students = []
        self.teachers = []

    def find_class(self, class_name):
        for c in self.classes:
            if c.name == class_name:
                return c
        return 0

    def add_class(self, class_name):
        if not self.find_class(class_name):
            self.classes.append(School_class(class_name))

    def classeslist(self):
        return [c.name for c in self.classes]

    def find_student(self, surname, name, midname):
        for s in self.students:
            if s.surname == surname and s.name == name and s.midname == midname:
                return s
        return 0

    def find_students(self, class_name):
        studentslist = []
        c = self.find_class(class_name)
        if c:
            for student in self.students:
                if student.school_class == c:
                    studentslist.append(student.shortname())
        return studentslist

    def add_student(self, surname, name, midname, father, mother, school_class):
        st = Student(surname, name, midname, father, mother, school_class)
        if st:
            self.students.append(st)
        return st

    def find_teacher(self, school_subject):
        for t in self.teachers:
            if t.school_subject == school_subject:
                return t
        return 0

    def add_teacher(self, surname, name, midname, school_subject):
        t = self.find_teacher(school_subject)
        if not t:
            t = Teacher(surname, name, midname, school_subject)
            self.teachers.append(t)
            return t
        else:
           return 0

    def add_subject(self, class_name, school_subject):
        t = self.find_teacher(school_subject)
        c = self.find_class(class_name)
        c.school_subjects.append(t)    

        
school = School()

school.add_class('5A')
school.add_class('5B')
school.add_class('5C')

father = Person('Иванов','Иван','Иванович')
mother = Person('Иванова','Инна','Ивановна')

school.add_student('Иванов','Кондрат','Иванович',father,mother, school.find_class('5B'))
school.add_student('Сидоров', 'Петр', 'Кедрович', Person('Сидоров', 'Кедр', 'Хренович'),
                   Person('Сидорова', 'Марфа', 'Петровна'), school.find_class('5A'))

school.add_teacher('Веснин', 'Юрий', 'Петрович', 'Математика')
school.add_teacher('Теорин', 'Квант', 'Полевич', 'Физика')
school.add_teacher('Заикин', 'Ипполит', 'Матвеевич', 'Литература')

school.add_subject('5A','Физика')
school.add_subject('5A','Математика')
school.add_subject('5B','Литература')
school.add_subject('5B','Литература')
school.add_subject('5C','Физика')
school.add_subject('5C','Математика')
school.add_subject('5C','Литература')


# 1. Получить полный список всех классов школы
print('Список классов:')
print(school.classeslist())
# 2. Получить список всех учеников в указанном классе
print('ученики 5A класса:')
print(school.find_students("5A"))
print('ученики 5B класса:')
print(school.find_students("5B"))
print('ученики 5C класса:')
print(school.find_students("5C"))

# 3. Получить список всех предметов указанного ученика 
print('список предметов ученика Иванов Кондрат Иванович:', school.find_student('Иванов', 'Кондрат', 'Иванович').school_class.subjectlist())
# 4. Узнать ФИО родителей указанного ученика
print('родители ученика Сидоров Петр Кедрович:', school.find_student('Сидоров', 'Петр', 'Кедрович').get_parents())
# 5. Получить список всех Учителей, преподающих в указанном классе
print('список преподающих в 5A классе:', school.find_class('5A').teacherslist())

