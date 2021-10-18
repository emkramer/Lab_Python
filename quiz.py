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
            print('новый уровень: ',o)
        kol = +1
        connection=sqlite3.connect('quiz_Q.sqlite')
        cursor=connection.cursor()
        number = random.choice(list_num)
        list_num.remove(number)
        cursor.execute('SELECT * FROM ALL WHERE id ='+ str(number) +';')
        r = cursor.fetchall()
        n = len(r)
        cursor.execute('SELECT ANSWER_RIGHT FROM ALL WHERE id ='+ str(number) +';')
        a = cursor.fetchall()
        r.remove(a)
        print(r)
        ans = str(input('НАПИШИТЕ БУКВУ С ПРАВИЛЬНЫМ ОТВЕТОМ'))
        if ans == a:
            print('ответ верный, ура')
        else:
            print('увы, но вы проиграли')
            break
        
