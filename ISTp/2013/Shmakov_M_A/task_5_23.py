# Задача 5. Вариант 23
# Напишите программу, которая бы при запуске случайным образом отображала
# имя одной из трех официальных жен Зевса.
# Shmakov M. A.
# 02.11.2016

import random
wifes = ["Метида", "Фемида", "Гера"]
number = random.randint(0, 2)
name = wifes[number]

print(name, "- имя жены Зевса")
input("\nНажмите Enter для выхода.")
