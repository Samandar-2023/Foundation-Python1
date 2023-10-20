# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 20:44:02 2023

@author: Samandar
"""
"""
avtolar = ['audi', "bmw", "volvo", "kia", "hyudai"]

for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())
        
ism = 'Ali'
ism.lower() == 'ali'


ism = input("Ismingizni kiriting?\n>>> ")
if ism.lower() != 'ali':
    print("Uzir biz Alini kutyapmiz")
else:
    print(f"Salom {ism}")
    


javob = float(input("12x6 nechiiga teng?\n>>> "))
if javob != float(12*6):
    print("Javob xato!")


yosh = int(input("Yoshingizni kiriting?>>> "))

if yosh >= 18:
    print("Xush kelibsiz!")
else:
    print("Kirishingiz mumkin emas!")
    



login = input("Yangi login tanlang:>>> ")
if len(login) <= 5:
    print("Login 5 harfdan ko'roq bo'lishi shart!")



yil = int(input("Yilingizni kiriting?>>> "))

if 2023-yil >= 18:
    print("Xush kelibsiz")
else:
    print(f"Siz {2023-yil} yoshda ekansiz sizga taqiqlanadi")


yosh = int(input("Yoshingiz nechida!>>> "))
if yosh > 65: print("Siz COVID-19 guruhida ekansiz")

x, y = 20, 25
print("x > y") if x > y else print("x < y")


"""


# Amaliyot

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

"""
for i in cars:
    if i != 'gm':
        print(i.title())
    else:
        print(i.upper())


ism = input("Ismingizni kiriting?>>> ")
if ism.title() == "Admin":
    print("Xush kelibsiz Admin, Foydalanuvchilar ro'yhatini ko'rasizmi")
else:
    print(f"Xush kelibsiz {ism.title()}!")
"""

son1 = int(input("1 chi sonni kiriting>>> "))
son2 = int(input("2 chi sonni kiriting>>> "))

if son1 == son2:
    print("Ikkala son ham teng")

son3 = int(input("Istalgan sonni kiriting>>> "))

if son3 > 0:
    print("Son musbat")
else:
    print("Son manfiy")
    
while True:
    son4 = int(input("Son kiriting>>> ")) 
    if son4 > 0:
        print(son4**2)
        break
    else:
        print("Musbat son kiriting")
    
    
    
    
    