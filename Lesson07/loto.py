#!/usr/bin/python3
__author__ = 'Salyakhutdinov Rustem'

help_string = """
def== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
"""
"""
Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

def convertNumStr(n):   #переводит  ненулевое число из диапазона (-99,99) к 
    s=''                #строке длиной 2
    if n>0:             #если число положительное то число
        s=str(n)
    elif n==0:          #если нулевое то пробел
        s=' '
    else:               #если отрицательное то прочерк
        s='-'
    return ' '+s if len(s)==1 else s

def replace(l,n):         #заменяет в списке первое совпавшее число на отрицательное    
    cl=l[:]               #по модулю можно восстановить то что было  
    for key, value in enumerate(l):
        if n==value:
            cl[key] = -n
    return cl        
            
class LottoCard:
    def __init__(self, name):
        self.name = name
        self.numbers=self.generate()
        self.originals=self.numbers[:]
    def generate(self):
        etalon=[0,0,0,0,1,1,1,1,1]              #список для расстановки чисел в строке
        nums =random.sample(range(1,91), k=15)  #получаем рандомный список 15 чисел от 1 до 90 
        card_fields=[]
        for i in range(3):      #нарезаем строки карточки
            temp_row=['']*9
            temp = sorted(nums[5*i:5*(i+1)],reverse = True) #выбираем по порядку по 5 чисел 
            random.shuffle(etalon)            #генерим рандомную расстановку
            for j, item in enumerate(etalon):
                if item==1:                     #если 1 то вписываем число
                    temp_row[j]=temp.pop()   
                else:                           #заполняем 0 
                    temp_row[j]=0
            card_fields.append(temp_row)
        return card_fields

    def check(self,barrel):
        """метод проверяет наличие номера в карточке и возвращает True/False"""
        for index, row in enumerate(self.numbers):
            if barrel in row:
                return True   
        return False 

    def cross(self,barrel):
        """метод зачеркивает номер в карточке и возвращает True/False"""
        for index, row in enumerate(self.numbers):
            if barrel in row:
                self.numbers[index]=replace(row,barrel) 
                return True 
        return False

    def get_uncross_count(self):
        """метод возвращает кол-во незачеркнутых номеров"""
        count = 0
        for row in self.numbers:
            count += len([i for i in row if i >0])
        return count
    
    def draw(self,start=False):
        """метод рисует карточку"""
        self.start=start
        x=len(self.name)
        a= (24-x)//2
        print('{0}{1}{2}{1}{3}'.format('-'*a,' ',self.name,'-'*(24-x-a)))   #header             
        if not self.start:
            card_list=self.numbers
        else:
            card_list=self.originals
        for num, value in  enumerate(card_list):        #ряд
            line =' '.join(map(convertNumStr, value))
            print(line)
        print('-'*26)       #footer

 
             
class BarrelBag:
    def __init__(self):
        self.bag = random.sample(range(1,91), k=90) 
        self.bag_out=[]
        
    def pull_out(self):
        """метод реализует выбор бочонка из мешка"""
        cur_barrel=self.bag.pop()
        self.bag_out.append(cur_barrel)
        return cur_barrel
    
    def get_count_left(self):
        """метод возвращает кол-во бочонков в мешке"""
        return len(self.bag)

class Player:
    def __init__(self, is_bot=True):
        self.is_bot = is_bot
        self.lottoCard = LottoCard('Карточка компьютера') if self.is_bot else LottoCard('Ваша Карточка')

    def step(self,barrel):
        """метод реализует ход игрока/компьютера. Возвращает False, если игрок неверно ответил на вопрос"""
        if self.is_bot:
            is_cross=self.lottoCard.check(barrel)   #Компьютер всегда зачеркивает верно
        else:   
            is_cross = input('Зачеркнуть цифру? (y/n)')=='y'
            
        if is_cross:                                #Если ответили да, пробуем вычеркнуть номер
            return self.lottoCard.cross(barrel)     
        elif self.lottoCard.check(barrel):          #Если ответили нет, проверяем наличие номера
            return False
        else:
            return True
        
class Lotto:
    def __init__(self):
        self.bag = BarrelBag()  
        self.round=1
        self.human=Player(False)
        self.bot=Player()

    def step(self):
        """метод реализует один раунд игры. Возвращает кортеж (bool,str) (Есть победитель, Имя победителя)"""
        barrel=self.bag.pull_out()      #вначале вытащим бочонок
        print('#######  ХОД № {} #######'.format(str(self.round)))
        print('Новый бочонок: {} (осталось {})'.format(str(barrel),str(self.bag.get_count_left())))
        self.human.lottoCard.draw()     #рисуем карточку игрока и компьютера
        self.bot.lottoCard.draw()       
        self.round +=1                  #счетчик раундов
        if not self.human.step(barrel): #ход Человека, если вернуло False то проиграли
            print ('Ты проиграл.')
            return True, 'Компьютер'
        self.bot.step(barrel)           #Ход Компьютера      
            
        if self.human.lottoCard.get_uncross_count()==0: #Проверка что все номера зачеркнуты
            return True, 'Ты'
        elif self.bot.lottoCard.get_uncross_count()==0:
            return True, 'Компьютер'
        else:
            return False, None
        
    def game(self):
        """основной метод игры . Вызываем метод step, пока он не вернет True и имя победителя"""
        print(welcome_string)
        is_end=False
        winner=None
        while not is_end:
            is_end, winner = self.step()
        print('{} победил'.format(winner))


welcome_string="""
___  ___ _____  _____   ___   
|  \/  ||  ___||  __ \ / _ \  
| .  . || |__  | |  \// /_\ \ 
| |\/| ||  __| | | __ |  _  | 
| |  | || |___ | |_\ \| | | | 
\_|  |_/\____/  \____/\_| |_/ 
                              
                              
 _      _____  _____  _____   
| |    |  _  ||_   _||  _  |  
| |    | | | |  | |  | | | |  
| |    | | | |  | |  | | | |  
| |____\ \_/ /  | |  \ \_/ /  
\_____/ \___/   \_/   \___/  
"""

def menu():
    print(' Выберите действие:')
    print(' 1 - Посмотреть правила')
    print(' 2 - Начать Новую Игру')
    print(' 3 - Посмотреть карточки игроков')
    print(' 4 - Проверить оставшиеся бочонки')
    print(' 5 - Выйти')
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
        print(help_string)
    elif action_flag == 2:
        lotto=Lotto()
        lotto.game()
    elif action_flag == 3:
        try:
            lotto.human.lottoCard.draw(True)
            lotto.bot.lottoCard.draw(True)
        except  NameError:
            print("Вы еще не сыграли")
    elif action_flag == 4:
        try:
            print(sorted(lotto.bag.bag))
        except  NameError:
            print("Вы еще не сыграли")
    elif action_flag == 5:
        print('Завершение работы.')
        break
    else:
        print('Неизвестное действие. Выходим.')
        break
