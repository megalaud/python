
__author__ = 'Salyakhutdinov Rustem'


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import hw05_lib as easy
     
    ###создание директорий dir_1 - dir_9
for i in range(1,10):
    dir_name=f'dir_{i}'
    easy.make_dir(dir_name)

    ###удаление директорий dir_1 - dir_9
for i in range(1,10):
    dir_name=f'dir_{i}'
    easy.remove_dir(dir_name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

def list_dir():
    work_dir = os.getcwd()
    return [d for d in os.listdir(work_dir) if  os.path.isdir(d)] #создаем список содержимого исключая файлы

print(list_dir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_filebody(source, dest, buffer_size=1024*1024):
    while True:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)

def copy_file(source, dest):
    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        copy_filebody(src, dst)

import sys
source=sys.argv[0]  
dest=f'{source}.copy'
copy_file(source, dest)
