
__author__ = 'Salyakhutdinov Rustem'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number = 432103786

while number>0:
    digital = number%10
    print(digital)
    number = number//10
   

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a=input("Введите значение первой переменной  ")
b=input("Введите значение второй переменной  ")

x=a
a=b
b=x

print("Новое значение первой переменной: ",a)
print("Новое значение второй переменной: ",b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите ваш возраст в годах  "))
if age>=18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
