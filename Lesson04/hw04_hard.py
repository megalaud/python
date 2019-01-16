# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

matrix_rotate = list(map(list, zip(*matrix)))
#print("rotate_matrix = ", matrix_rotate)


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
import random
number  = int(''.join(map(str,[random.randint(0,9) for i in range(1000)]))) #Генерируем число
"""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

def mult(x):    #произведение всех цифр строки
    res=1
    for i in x:
        res *=int(i)
    return res    

print(number)   #выводим сгенерированное число
str_number=str(number)
number_list=[str_number[num:num+5] for num, item in enumerate(str_number) if num<len(str_number)-4] #генерируем список пятерок
temp_num=0
temp_item=0
for num, item in enumerate(number_list):
    x = ( mult(item),num) if  mult(item)>temp_item else (temp_item, temp_num) #возвращаем произведение и индекс
    temp_num=x[1]
    temp_item=x[0]
print(x)



# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
NO = {
    1: [0, 6],
    2: [1, 3],
    3: [2, 1],
    4: [3, 7],
    5: [4, 5],
    6: [5, 0],
    7: [6, 2],
    8: [7, 4],
}


        
#queens = NO            #для проверки расстановки при которой ферзи не бьют друг друга
queens = {}
for i in range(1, 9):
    queens[i] = [int(f)-1 for f in input(f'Ведите положение Ферзя {i} (две цифры разделенные пробелом)').split(' ')]
#print (queens)

matrix_board=[[0 for i in range(8)] for j in range(8)] #расставляем ферзей на поле
for n, p in queens.items():
    matrix_board[p[1]][p[0]]=1

    #выводим визуальную картинку поля
print("   1  2  3  4  5  6  7  8")
for i, line in enumerate(matrix_board):     
    print("{} {}".format(i+1, matrix_board[i]))

max_row = len(matrix_board)
max_col = len(matrix_board[0])
cols = [[] for i in range(max_col)]         #список столбцов
rows = [[] for i in range(max_row)]         #список линий
fdiag = [[] for i in range(max_col + max_row - 1)]  #список прямых диагоналей
bdiag = [[] for i in range(len(fdiag))]     #список обратных диагоналей
min_bdiag = -max_col + 1
    #строим списки
for y in range(max_row):
    for x in range(max_col):
        rows[y].append(matrix_board[y][x])
        cols[x].append(matrix_board[y][x])
        fdiag[x+y].append(matrix_board[y][x])
        bdiag[-min_bdiag+x-y].append(matrix_board[y][x])

check_rows=0             #счетчик линий
check_cols=0           #счетчик столбцов
check_fdiag=0           #счетчик диагоналей прямых
check_bdiag=0       #счетчик диагоналей обратных

#Если сумма значений по каждому столбцу/строк/диагонали не превышает 1 значит
#в них не более одного ферзя и они не под ударом.

for i, line in enumerate(cols):
    check_cols = check_cols+1 if sum(line)>1 else check_cols
for i, line in enumerate(rows):
    check_rows = check_rows+1 if sum(line)>1 else check_rows
for i, line in enumerate(fdiag):
    check_fdiag = check_fdiag+1 if sum(line)>1 else check_fdiag
for i, line in enumerate(bdiag):
    check_bdiag = check_bdiag+1 if sum(line)>1 else check_bdiag    

rezult = 'NO' if  check_rows==check_cols==check_fdiag==check_bdiag==0 else 'YES'
print(rezult)
