
__author__ = 'Salyakhutdinov Rustem'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import sys
import os
import hw05_lib as easy
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение содержимого текущей директории")
    print("pwd - отображение полного пути текущей директории")  #В оригинале тут был ls , но pwd более привычна
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        file_name = dir_name
        copy_name=f'{file_name}.copy'
        easy.copy_file(file_name,copy_name)
        print('Создан файл {} - копия файла {}'.format(copy_name,file_name))
    except FileNotFoundError:
        print('Файла с именем {} не существует'.format(file_name))
    except PermissionError:
        print('Доступ запрещен')

def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        file_name = dir_name
        if input('Вы уверены, что хотите удалить файл {}.(Y/N)'.format(file_name))=='Y':
            os.remove(file_name)
            print('Файла с именем {} был удален'.format(file_name))
        else:
            print('Подтверждение не получено. Файла с именем {} не был удален'.format(file_name))
    except FileNotFoundError:
        print('Файла с именем {} не существует'.format(file_name))


def change_dir():
    if not dir_name:
        print("Необходимо указать директорию вторым параметром")
        return
    try:
        if os.path.isabs(dir_name):
            dir_path=dir_name
        else:
            dir_path = os.path.join(os.getcwd(), dir_name)
        os.chdir(dir_path)
        print('Выполнен переход в директорию {}'.format(os.getcwd()))
    except OSError as e:    #универсальный обработчик ошибок
        print("Error: %s - %s." % (e.filename, e.strerror))
def list_dir():
    print('==========СПИСОК ДИРЕКТОРИЙ========')
    print ([d for d in os.listdir(os.getcwd()) if os.path.isdir(d)])
    print('==========список файлов========')
    print ([d for d in os.listdir(os.getcwd()) if os.path.isfile(d)])

def work_dir():
    print(os.getcwd())
def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": list_dir,
    "pwd": work_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
