
__author__ = 'Salyakhutdinov Rustem'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
def length(Ax,Ay,Bx,By):
    l = (((Bx - Ax)**2 + (By - Ay)**2)**(1/2))
    return l
class Triangle():
    """
    Класс для фигуры-треугольника
    """
    def __init__(self, coords_A, coords_B, coords_C ):
        self._Ax = coords_A[0]
        self._Ay = coords_A[1]
        self._Bx = coords_B[0]
        self._By = coords_B[1]
        self._Cx = coords_C[0]
        self._Cy = coords_C[1]
        self._AB = length(self._Ax,self._Ay,self._Bx,self._By)
        self._BC = length(self._Bx,self._By,self._Cx,self._Cy)
        self._CA = length(self._Cx,self._Cy,self._Ax,self._Ay)

    def calc_perimetr(self):
        return self._AB+self._BC+self._CA
    def calc_square(self):
        """
        S=(p*(p-a)*(p-b)*(p-c))^(1/2),  p - полупериметр, a,b,c - стороны
        """
        p=self.calc_perimetr()/2
        return (p*(p-self._AB)*(p-self._BC)*(p-self._CA))**(1/2)
    def calc_altitude(self, top):
        if top=='A':
            return self.calc_square()*2/self._BC
        elif top=='B':
            return self.calc_square()*2/self._CA
        elif top=='C':
            return self.calc_square()*2/self._AB        
        else:
            return None        
    def info(self):
         print("Стороны треугольника ABC: AB {} , BC {} , CA {} ".format(self._AB,self._BC,self._CA))      
         print("Площадь треугольника ABC равна {}".format(self.calc_square()))
         print("Периметр треугольника ABC равен {}".format(self.calc_perimetr()))
         print("Высоты треугольника: из A {}, из B {}, из С {} ".format(self.calc_altitude('A'),self.calc_altitude('B'),self.calc_altitude('C')))
         
a=Triangle((1,0),(5,4),(3,6))
a.info()

        
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqualTrapeze():
    """
    Класс для фигуры "Равнобочная трапеция"
    """
    def __init__(self, coords_A, coords_B, coords_C, coords_D ):
        self._Ax = coords_A[0]
        self._Ay = coords_A[1]
        self._Bx = coords_B[0]
        self._By = coords_B[1]
        self._Cx = coords_C[0]
        self._Cy = coords_C[1]
        self._Dx = coords_D[0]
        self._Dy = coords_D[1]
        self._AB = length(self._Ax,self._Ay,self._Bx,self._By)
        self._BC = length(self._Bx,self._By,self._Cx,self._Cy)
        self._CD = length(self._Cx,self._Cy,self._Dx,self._Dy)
        self._DA = length(self._Dx,self._Dy,self._Ax,self._Ay)

    def _check(self):
        #case1
        scalar1=(self._Bx-self._Ax)*(self._Dx-self._Cx)+(self._By-self._Ay)*(self._Dy-self._Cy)  #Скалярное произведение векторов AB и CD
        mod_mult1=self._AB*self._CD   #произведение модулей векторов AB и CD
        #case2
        scalar2=(self._Cx-self._Bx)*(self._Ax-self._Dx)+(self._Cy-self._By)*(self._Ay-self._Dy)  #Скалярное произведение векторов BC и DA
        mod_mult2=self._BC*self._DA   #произведение модулей векторов BC и DA
        if (abs(scalar1) == mod_mult1) and (self._BC==self._DA):
            return 1 
        elif (abs(scalar2) == mod_mult2) and (self._AB==self._CD):
            return 2 
        else:
            return 0
    def is_trapeze_equal(self):
        return self._check()>0

    def calc_legs(self):
        return [self._AB,self._BC,self._CD,self._DA]

    def calc_perimetr(self):
        return self._AB+self._BC+self._CD+self._DA

    def calc_square(self):
        if self._check()==1:
            a, b, c = self._AB, self._CD, self._BC
        elif self._check()==2:   
            a, b, c = self._BC, self._DA, self._AB
        else:
            a,b,c=0,0,0
        return ((a+b)/2)*((c**2-((a-b)**2)*(1/4))**(1/2))
    def info(self):
         print("Стороны трапеции ABCD: AB {} , BC {} , CD {}, DA {} ".format(self._AB,self._BC,self._CD,self._DA))      
         print("Площадь трапеции ABCD равна {}".format(self.calc_square()))
         print("Периметр трапеции ABCD равен {}".format(self.calc_perimetr()))

   
                
b= EqualTrapeze((0,0),(0,6),(4,5),(4,1))
print('Трапеция равнобедренная? ' + str(b.is_trapeze_equal()))
b.info()
