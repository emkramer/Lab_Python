#пишем игру викторину
#1)минимум 5 уровне
#2)минимум по 4 варианта ответа
#3)GIT
#4)Работает с БД
#5)адекватные вопросы
#random, sqlite3

import sqlite3
import time
import random


list_quest = []
list_num = [1,2,3,4,5]
k = 0
o = 0
x = input('начинаем игру? ="g"' )
if x != "g":
     print("всего хоро-ше-го!!!")
else:
    while True:
        if k % 2 ==0:
            o +=1
            print('новый уровень: ',0)
        kol = +1
        connection=sqlite3.connect('quiz_Q')
        give_out=connection.give_out()
        number = random.choice(list_num)
        remove.list_num(number)
        give_out.execute('SELECT * WHERE id =' + str(number) + ";")
        r = give_out.fetchall()
        print(r)
        ans = str(input('НАПИШИТЕ БУКВУ С ПРАВИЛЬНЫМ ОТВЕТОМ'))
        
        
        
        
    
    















