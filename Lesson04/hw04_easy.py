# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
origin_list = [random.randint(-100,100) for i in range(10)] #Генерируем рандомный список
print("Исходный список : {}".format(origin_list))
quad_list =[i**2 for i in origin_list]
print("Исходный список в квадрате : {}".format(quad_list))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits = ['fruit_1','fruit_11',
    'fruit_2','fruit_12',
    'fruit_3','fruit_13',
    'fruit_4','fruit_14',
    'fruit_5','fruit_15',
    'fruit_6','fruit_16',
    'fruit_7','fruit_17',
    'fruit_8','fruit_18',
    'fruit_9','fruit_19',
    'fruit_10','fruit_20']

list_fruits1=random.choices(fruits,k=8)  #Генерируем 2 рандомных списка
list_fruits2=random.choices(fruits,k=8)
list_union=[i for i in list_fruits1 if i in list_fruits2]

print("1 список : {}".format(list_fruits1))
print("2 список : {}".format(list_fruits2))
print("Пересечение : {}".format(list_union))
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

int_list = [random.randint(-100,100) for i in range(30)] #Генерируем рандомный список

print("Исходный список : {}".format(int_list))
edit_list =[i for i in int_list if i%3==0 and i>0 and i%4 !=0 ]
print("отфильтрованный список  : {}".format(edit_list))
