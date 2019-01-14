
__author__ = 'Salyakhutdinov Rustem'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def gcd(x, y):
    """ функция возвращает НОД чисел x и y """
    while y != 0:
        (x, y) = (y, x % y)
    return x
 
def oper(a, b, c, d, act):
    """ функция выполняет действие(act) с дробями a/b и с/d, а затем приводит сокращение на НОД"""
    if act=='+':
        x = a*d + b*c
    else:
        x = a*d - b*c
    y = b*d
    z = gcd(x, y)
    return (x//z, y//z)

def drob(x):
    """на вход подается дробь вида -2 4/5, на выходе (a,b) -пара числитель и знаметатель приведенной дроби """
    sign=lambda x:-1 if x=='-' else 1
    if sign(x[0])==-1:
        s=x[1:]
    else:
        s=x
        
    index_n=s.find(' ')
    if index_n>0:
        n = int(s[:index_n])
        s = s[index_n+1:]
        index_drob = s.find('/')
    else:
        index_drob = s.find('/')
        if index_drob==-1:
            n = int(s)
        else:
            n=0

    #index_drob = s.find('/')
    if index_drob>0:
        a,b = int(s[:index_drob]),int(s[index_drob+1:])
    else:
        a,b = 0,1
    a = sign(x[0]) *( n * b + a)
    return a,b

def anti_drob(x,y):
    """функция к drob(x). на вход (x,y) -пара числитель и знаметатель приведенной дроби .
    На выходе строка вида -2 4/5,  """
    if (x // y)==0:
        return  str(x)+'/'+str(y)
    else:
        return  str(x//y)+' '+str(abs(x)%y)+'/'+str(y)
 

def drobinator(x):
    """
    Функция парсит выражение с дробями x (строка) и возвращает результат (строку)
    """
    operations=('+','-')

    index_oper = x.find("+")
    if index_oper>0:
        operation=operations[0]
    else:
        index_oper = x.find("-",1)
        operation=operations[1]

    a= x[:index_oper].strip()
    b= x[index_oper+1:].strip()
    a,b = drob(a),drob(b)
    new_a, new_b = oper(a[0],a[1],b[0],b[1],operation)
    return anti_drob(new_a,new_b)


print(drobinator('5/6 + 4/7'))
print(drobinator('-2/3 - -2'))
print(drobinator('7/8 - 3 135/157'))
print(drobinator('362/13 - -135/157'))



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


"""Результат выводим в файл "data/money" """
import os

workers=[]
hours=[]
path = os.path.join('data', 'workers')
with open(path, 'r', encoding='UTF-8') as f:
    rows=f.readlines()
    for s in rows[1:]:
       workers.append(dict(firstname=s[0:7].strip(),sirname=s[8:20].strip(),salary=int(s[21:35].strip()),position=s[36:51].strip(),norm=int(s[52:].rstrip())))
   # print(workers)
path = os.path.join('data', 'hours_of')
with open(path, 'r', encoding='UTF-8') as f:
    rows=f.readlines()
    for s in rows[1:]:
       hours.append(dict(firstname=s[0:7].strip(),sirname=s[8:20].strip(),worked=int(s[21:].rstrip())))
  #  print(hours)

def get_money_data(x,y):
    for line in workers:
        fname=line.get('firstname')
        sname=line.get('sirname')
        if (x==fname)&(y==sname):
            a=line.get('salary')
            b=line.get('norm')

    return a,b

def money(x,y,z):
    #x-зарплата
    #y-норма времени
    #z-отработаные часы

    if z<y:
        mon=x*(z/y)
    else:
        mon=x*(2*(z/y)-1)
    return round(mon,2)

path = os.path.join('data', 'money')
my_file = open(path, "w", encoding='UTF-8')
my_file.write('Имя     Фамилия      Заработано денег\n')
for line in hours:
    fname, sname =line.get('firstname'),line.get('sirname')
    salary, norm = get_money_data(fname, sname)
    work_money = money(salary,norm,line.get('worked'))
    my_line=''
    my_line+=fname+' '*(8-len(fname))
    my_line+=sname+' '*(13-len(sname))
    my_line+=str(work_money)+' '*(16-len(str(work_money)))
    my_file.write(str(my_line)+'\n')
my_file.close()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os
OUTPUT_DIR = 'data\\fruits_output'
DEFAULT_NAME = 'fruits_'

def clear_dir():
    if not os.path.isdir(OUTPUT_DIR):
        return
    for i in os.listdir(OUTPUT_DIR):
        file = f'{OUTPUT_DIR}\\{i}'
        if os.path.isfile(file):
            os.remove(file)

def write_fruit_into_file(fruit):
    char = fruit[0]
    filename = f'{OUTPUT_DIR}\\{DEFAULT_NAME}{char}.txt'
    if not os.path.isfile(filename):
        flag = 'w'
    else:
        flag = 'a'
    with open(filename, flag, encoding='UTF-8') as f:
        f.write(f'{fruit}\n')

if not os.path.isdir(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
else:
    clear_dir()
    
path = os.path.join('data', 'fruits.txt')
with open(path, 'r', encoding='UTF-8') as f:
    rows=f.readlines()
    for line in rows:
        if not (not line or line.isspace()):
            write_fruit_into_file(line)
