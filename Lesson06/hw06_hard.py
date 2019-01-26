
__author__ = 'Salyakhutdinov Rustem'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker():
    name = None
    surname = None
    salary = 0
    position = None
    norm = 0
    worked = 0
    money =0
    
    def __init__(self, line):
        self.get_data(line)
        
    
    def get_data(self, data):
        self.name = data[0:7].strip()
        self.surname = data[8:20].strip()
        self.position = data[36:51].strip()
        self.salary =int(data[21:35].strip())
        self.norm=int(data[52:].rstrip())    
    
    def get_fullname(self):
        return '{} {}'.format(self.name, self.surname)

    def get_money(self):
        if self.worked<self.norm:
            mon=self.salary*(self.worked/self.norm)
        else:
            mon=self.salary*(2*(self.worked/self.norm)-1)
        return round(mon,2)

    def info(self):
        info0 = '++++++++'
        info1 = 'Работник: {}'.format(self.get_fullname())
        info2 = 'Должность(Оклад): {}({})'.format(self.position, self.salary)
        info3 = 'Отработал/Норма: {}/{}'.format(self.worked, self.norm)
        info4 = 'Заработал: {}'.format(self.get_money())

        print (info0+'\n'+info1+'\n'+info2+'\n'+info3+'\n'+info4)

class Hours():
    name = None
    surname = None
    worked = 0

    def __init__(self, line):
        self.get_data(line)

    def get_data(self, data):
        self.name = data[0:7].strip()
        self.surname = data[8:20].strip()
        self.worked =int(data[21:].rstrip())   

    def get_fullname(self):
        return '{} {}'.format(self.name, self.surname)
        
def read_files(workers_path, hours_path):

    workers = []
    with open(workers_path, 'r', encoding='utf-8') as file:
        for line in file.readlines()[1:]:
            workers.append(Worker(line))
    hours = []
    with open(hours_path, 'r', encoding='utf-8') as file:
        for line in file.readlines()[1:]:
            hours.append(Hours(line))

    for h in hours:
        cur_worker = h.get_fullname()
        for w in workers:
            if cur_worker==w.get_fullname():
                w.worked = h.worked
            else:
                pass
    return workers

workers_path=os.path.join('data', 'workers')
hours_path=os.path.join('data', 'hours_of')
workers = read_files(workers_path, hours_path)
for w in workers:
    w.info()


