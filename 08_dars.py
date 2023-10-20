# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:07':39 2023

@author:' Samandar
"""
'''
cars = ['bmw', 'mercadec benz', 'Volvo', 'general motors', 'toyoto']

sonlar = list(range(1, 11))
print(sonlar)

toq = list(range(1, 10, 2))
print(toq)

juft = list(range(2, 20, 2))
print(juft)

sanash = list(range(0, 101, 10))
print(sanash)


narhlar =  [12000, 225000, 23456, 98000, 9934, 32874]
'''


# Tuple

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard', 'lizard')



# Amaliyot

davlatlar = ['Uzbekistan', 'India', 'USA', 'Korea', 'China', 'Turkey']

print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
s = davlatlar.reverse()
print(s)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)


sonlar = list(range(120, 1200, 2))
print(sum(sonlar))
print(max(sonlar) - min(sonlar))
print(len(sonlar))
print(sonlar[len(sonlar) // 2:])



taomlar = ['osh', 'jarkob', 'shovla', 'shorva', 'xonim']
nonushta = taomlar[::]
del nonushta[1:3]
nonushta.append('Kabob')
nonushta.append('Somsa')
print("Taomlar: ", taomlar)
print("Nonushta: ", nonushta)

nonushta[0] = "qaymoq va non"
nonushta = tuple(nonushta)
print("In Tuple : ", nonushta)