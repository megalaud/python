__author__ = 'Salyakhutdinov Rustem'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
num_list = [int(str) for str in input('Введите целые числа через запятую').split(',')]
print('Список чисел: ', num_list)
new_list=[]
for num in num_list:
    if num>=0:
        root=math.sqrt(num)
        #print (root)
        if str(root).split('.')[1]=='0':
            new_list.append(int(root))

print('Новый список чисел: ', new_list)                
               


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', \
        'августа', 'сентября', 'октября', 'ноября', 'декабря']

days = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое',
        'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое',
        'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 
        'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое',
        'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']

date = input('Введите дату в формате dd.mm.yyyy, например: 02.11.2013 : ')

day = int(date.split('.')[0])
month = int(date.split('.')[1])
year = int(date.split('.')[2])

day = days[day-1]
month= months[month-1]

print('{0} {1} {2} года'.format(day, month, year))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input('Введите кол-во элементов: '))
random_list=[]
for c in range(n):
    random_list.append(random.randint(-100,100))
print ('список произвольных чисел : ',random_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

num_list = [int(str) for str in input('Введите целые числа через запятую').split(',')]
print('Список чисел: ', num_list)
list_a=[]
for c in num_list:
    if c in list_a:
        continue
    else:
        list_a.append(c)
print('Неповторяющиеся элементы исходного списка: ', list_a)

list_b=[]
for c in num_list:
    count=0
    for cc in num_list:
        if c==cc:
            count+=1
    if count==1:
        list_b.append(c)
print('Элементы исходного списка, которые не имеют повторений: ', list_b)    


