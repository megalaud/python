
__author__ = 'Salyakhutdinov Rustem'


# функции необходимые для решения заданий EASY и NORMAL

import os
def make_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана.'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует.'.format(dir_name))

def remove_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.removedirs(dir_path)
        print('Директория {} удалена.'.format(dir_name))
    except FileNotFoundError:
        print('Директория {} не найдена. Проверьте правильность указания имени.'.format(dir_name)) 
    except OSError:
        print('Что то пошло не так c директорией {}.'.format(dir_name))
       
def change_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('Перешли в директорию {}'.format(dir_name))
    except FileNotFoundError:
        print('Ошибка перехода : Директории {} не существует'.format(dir_name))

def copy_filebody(source, dest, buffer_size=1024*1024):
    while True:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)

def copy_file(source, dest):
    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        copy_filebody(src, dst)