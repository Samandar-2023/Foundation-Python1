'''
son = 50
if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")

yosh = int(input("Yoshingizni kiriting:>>>  "))

if yosh <= 4:
    print('Sizga kirish bepul.')
elif yosh <= 12:
    print("Sizga kirish 5000 so'm.")
elif yosh <= 18:
    print("Sizga kirish 8000 so'm")
else:
    print("Sizga kirish 10000 so'm")

# Or

if yosh <= 4:
    narh = 0 
elif yosh <= 12:
    narh = 5000
elif yosh <= 18:
    narh = 8000
else:
    narh = 10000
print(f"Sizga kirish {narh} so'm")


harorat = float(input("Haroratni kiriting?>>> "))
kun = input("Bugun nima kun?>>> ")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print("Bugun dam olish kuni")
if kun.lower() == 'yakshanba' and harorat >= 30:
    print("Cho'milgani kettik")
if kun.lower() == 'yakshanba' and harorat < 30:
    print('Uyda dam olamiz')
'''
'''
# Boolean

narh = 15000
choy = True
salat = True

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
print(f"Umumiy hisob {narh}")


narh = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False

if salat:
    narh += 5000
    print("Mijoz salat oldi.")
if non:
    narh += 2000
    print("Mijoz non oldi.")
if choy:
    print("Mijoz choy oldi.")
    narh += 3000
if kompot:
    print("Mijoz kompot oldi.")
    narh += 5000
if assorti:
    print("Mijoz assorti oldi")
    narh += 15000
print(f"Jami hisob {narh} so'm")

'''

'''
# in operation
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']

ovqat = input("Nima ovqat buyirasiz?>>>  ")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi")
else:
    print("Afsuski bizda bu ovqat yo'q")
'''
'''
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")

'''

# Amaliyot

'''
son = int(input('Iltimos juft son kiriting>>> '))
if son % 2 == 0:
    print("Rahmat")
else:
    print("Bu juft son emas")
'''
'''
yosh = int(input("Yoshingizni kiriting>>> "))
narh = 0
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh <= 18:
    narh = 10000
elif yosh > 18:
    narh = 20000
print(f"Sizga kirish {narh} so'm")

'''
'''
son1 = float(input("Birinchi sonni kiriting>>> "))
son2 = float(input("Ikkinchi sonni kiriting>>> "))
if son1 > son2:
    print(f"{son1} > {son2}")
elif son1 < son2:
    print(f"{son1} < {son2}")
else:
    print(f"{son1} == {son2}")
'''

'''

mahsulotlar = ['banan', "go'sht", "sabzi", "olma", "kartoshka", "tarvuz", "non", "sholg'om", "anor", "tarvuz"]

savat = []
yoqlar = []

for i in range(5):
    savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
        yoqlar.append(mahsulot)
print(f"Do'konimizda {yoqlar} yo'q")

'''
'''
foydalanuvchilar = ['anvar', "samandar", "rovshan", 'sobir', "kamoliddin"]
login = input("Yangi login tanlang: ")
if login.lower() not in foydalanuvchilar:
    print("Xush kelibsiz!")
else:
    print("Login band, yangi login tanlang")

'''
'''
son = int(input("Istalgan butun son kiriting: "))
for i in range(1+1, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
        

'''











