﻿#Задача №10, Вариант 30
 #Напишите программу "Генератор персонажей" для игры.Пользователю должно быть предоставлено 30 пунктов, 
 #которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. 
 #Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, 
 #которым он решил присвоить другие значения.
 
# SHEIKO R.V
# 02.06.2016
 
print ("""
 			Добро пожаловать в "Генератор персонажей". 
 		Вы можете распределить 30 очков между 4 характеристиками:
 	Сила, Здоровье, Мудрость и Ловкость. Вы можете как и брать из общего
 числа пункотв, так и возвращать. Распределяйте характеристики с умом. Удачи!
 	""")
STR=0
HP=0
INT=0
AGL=0
point=30
number=0
print("Если хотите изменить Силу, то напишите 'Сила'. Если Здоровье, то 'Здоровье'. Если  Мудрость, то 'Мудрость'. Если к Ловкость, то 'Ловкость'.")
while True:
	if STR<0 or HP<0 or INT<0 or AGL<0 or point>30:
		print("Ошибка")
		break
		#number=int(input("Напишите снова"))
	elif point==0:
		print("Вы распределили очки. Их распределение:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL)
		break
	print("Ваши очки:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL,"\nНераспределённые очки:",point)
	user_input=input("")
	if user_input=="Сила" :
		number=int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point :
			STR+=number
			point-=number
		else :
			print('Слишком много')
	elif user_input=="Здоровье":
		number=int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point :
			HP+=number
			point-=number
		else :
			print('Слишком много')
	elif user_input=="Мудрость":
		number=int(input("Сколько хотите прибавить (отбавить)?"))
		if number <= point :
			INT+=number
			point-=number
		else :
			print('Слишком много')
	elif user_input=="Ловкость":
		number=int(input("Сколько хотите прибавить (отбавить)?"))
		if chislo <= point :
			AGL+=number
			point-=number
		else :
			print('Слишком много')
input("Нажмите Enter для выхода.")