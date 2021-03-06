
__author__ = 'Salyakhutdinov Rustem'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_lib as easy

def menu():
    print(' Выберите действие:')
    print(' 1 - Перейти в папку')
    print(' 2 - Просмотреть содержимое текущей папки')
    print(' 3 - Удалить папку')
    print(' 4 - Создать папку')
    print(' 5 - Выйти из утилиты')
    try:
        num = int(input('Ваш выбор? : '))
    except ValueError:
        print('Введите число')
        num = menu()
    return num

action_flag = 0
while action_flag != 5:
    action_flag=menu()
    if action_flag == 1:
        easy.change_dir(input('Введите имя директории в которую перейти: '))
    elif action_flag == 2:
        print('Содержимое текущей директории: ')
        print(os.listdir(os.getcwd()))
    elif action_flag == 3:
        easy.remove_dir(input('Введите имя директории для уделения: '))
    elif action_flag == 4:
        easy.make_dir(input('Введите имя директории для создания: '))
    elif action_flag == 5:
        print('Завершение работы.')
        break
    else:
        print('Неизвестное действие. Выходим.')
        break
