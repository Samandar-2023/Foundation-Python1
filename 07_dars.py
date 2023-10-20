# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:50:02 2023

@author: Samandar
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [12000, 18000, 10900, 22000, 25000, 36000]

sonlar = ['bir', 'ikki', 3, 4, 5]

#print(sonlar)

ismlar = []

# append

ismlar.append("Anvar")
ismlar.append("Sobir")
ismlar.append("Samandar")
ismlar.append("Kamoliddin")
ismlar.append("Rovshan")
ismlar.append("Ulug'bek")
print(ismlar)

# pop 

bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]

x = bozorlik.pop()
print(bozorlik)
print(x)





# Amaliyot

ismlar = ["Sobir", "Anvar", "Rovshan", "Kamoliddin", "Ulug'bek"]

for i in ismlar:
    print(f"Salom {i} , bugun choyxona bormi?")



sonlar = [1, 2, 3, 2.2, 4.5, 6.6, -23, -35]
sonlar[0] = sonlar[-1] + sonlar[-3]
sonlar[1] = sonlar[4] + sonlar[5]
print(sonlar)
sonlar.remove(-23)
sonlar.remove(-35)
print(sonlar)
sonlar.pop()
sonlar.pop()
print(sonlar)



t_shaxslar = ['Amir Temur', 'Beruniy', 'Islom Karimov', 'Shayh Muhammad Sodiq Muhammad Yusuf']
z_shaxslar = ['Elon Mask', 'Dr Zakir Naik', 'Shahruhkhan']

for i, j in zip(t_shaxslar, z_shaxslar):
    print(f"Men tarixiy shaxslardan {i} bilan, Zamonaviy shaxslardan esa {j} bilan suhbat qilishni istar edim")


friends = []
for i in range(4):
    friends.append(input(">>> "))

print(friends)

friends.insert(2, 'Muzaffar')
friends.remove('Anvar')
print(friends)

mehmonlar = []


    





