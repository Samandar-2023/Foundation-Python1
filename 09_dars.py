# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 20:16:03 2023

@author: Samandar
"""
"""
mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
 
for mehmon in mehmonlar:
    print("Salom ", mehmon)
    
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan Palonchiyevlar oilasi")
    
sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")


sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print(" 5 ta eng yaqin do'stlaringiz kim?")
for n  in range(5):
    dostlar.append(input(f"{n+1}- do'stingizni kiriting>>> ").title())
print(dostlar)
"""


# Amaliyot

son = 0
ismlar = ["Anvar", "Kamoliddin", 'Sobirjon', "Rovshan", "Saidakbar"]
for ism in ismlar:
    son += 1
    print(f"Do'stim {ism} tinchmisan")

print(f"Kod {son} martta takrorlandi")


t_sonlar = list(range(11, 100, 3))
for son in t_sonlar:
    print(son**3)

kinolar = []
for n in range(5):
    kinolar.append(input(f"{n+1} kino nomi >>> ").title())
print(kinolar)


odamlar = []
son = int(input("Bugun nechi kishi bilan suhbat qildingiz?>>> "))
for i in range(son):
    odamlar.append(input(f"{i+1}-suhbat qilgan odamingiz kim edi: ").title())
print(odamlar)