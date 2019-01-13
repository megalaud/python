
__author__ = 'Salyakhutdinov Rustem'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """Функция, возвращает ряд Фибоначчи в виде списка с n-элемента до m-элемента.
    Реализован только случай когда n<=m"""
    fib_list = []
    f = 1
    fib_list.append(f)
    fib_list.append(f) #2 первых элемента ряда  числа 1 1
    for i in range(2,m): #вычисляем и заполняем список рядом до m-элемента
        f = fib_list[-1] + fib_list[-2]   
        fib_list.append(f)
    return fib_list[n-1:]

print(fibonacci(1, 10))
print(fibonacci(5, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """Функция сортирует список по возрастанью методом пузырька
    """
    t_list=origin_list
    for n in range(1,len(t_list)):
        for i in range(len(t_list) - n):
            if t_list[i] > t_list[i + 1]:
                t_list[i], t_list[i + 1] = t_list[i + 1], t_list[i]
    return t_list
        
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func,a):
    b=[]
    for i in range(len(a)):
        if bool(func(a[i])) != False:
            b.append(a[i])
    return b

print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
print(list(my_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
print(list(filter(len, ['', 'not null', 'bla', '', '10'])))
print(list(my_filter(len, ['', 'not null', 'bla', '', '10'])))
            


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def  is_parallelogram(A1=(0,0),A2=(0,0),A3=(0,0),A4=(0,0)):
    """
    Возвращает 0 если параллелограм построить нельзя
    """
    def vector(A=(0,0),B=(0,0)):
        """на вход передаются координаты 2ух точек A(x1,y1) и B(x2,y2)
        На выходе получаем координаты вектора AB (x2-x1,y2-y1)"""
        vec=(B[0]-A[0],B[1]-A[1])
        return vec
    def sum_vector(A,B):
        """на вход передаются координаты 2ух векторов A(x1,y1) и B(x2,y2)
        На выходе получаем координаты результирующего вектора A+B (x1+x2,y1+y2)"""
        sum_vec=(B[0]+A[0],B[1]+A[1])
        return sum_vec
    def check_zero_angle(A,B):
        """на вход передаются координаты 2ух векторов A(x1,y1) и B(x2,y2)
        Проверяем угол между векторами на 0 и 180 градусов. На выходе получаем 0 если проверка успешна
        #ToDo можно добавить проверку на 90 градусов и тогда сможем определять что паралелограм является прямоугольником"""
        scalar=B[0]*A[0]+B[1]*A[1]      #Скалярное произведение векторов A и B
        mod_mult=((A[0]**2+A[1]**2)*(B[0]**2+B[1]**2))**(1/2)   #произведение модулей векторов A и B
        if scalar == mod_mult:
            return 0
        else:
            return 1
    # 4 точки можно соединить замкнутой ломаной линией 3 способами A1A2A3A4, A1A2A4A3, A1A3A2A4
    A=A1,A1,A1
    B=A2,A2,A3
    C=A3,A4,A2
    D=A4,A3,A4
    null_vec=(0,0)  #нулевой вектор
    check=0
    for i in range(3):  
       # print(A[i],B[i],C[i],D[i])
        AB=vector(A[i],B[i])
        BC=vector(B[i],C[i])
        CD=vector(C[i],D[i])
        DA=vector(D[i],A[i])
        if  (sum_vector(AB,CD) == null_vec)&(sum_vector(BC,DA) == null_vec)&(check_zero_angle(AB,BC)):
            check+=1
    return check
            
         
         
print(bool(is_parallelogram((0,1),(2,3),(4,5),(6,7))))
print(bool(is_parallelogram((0,0),(0,0),(0,0),(0,0))))
print(bool(is_parallelogram((0,0),(1,3),(4,-1),(5,2))))

    

    
