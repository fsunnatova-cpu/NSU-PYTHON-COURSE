"""
============================================================
NSU Python — Lab 06
Funksiyalar qiymat sifatida: lambda, saralash, filtrlash, map
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 24 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar
- Task 13-14: bonus
- Task 15-24: qo'shimcha mashqlar

ASOSIY TUSHUNCHALAR:
--------------------
- Funksiyalar ham qiymat (obyekt) -> o'zgaruvchiga saqlash mumkin
- Yuqori tartibli funksiya (higher-order) -> funksiyani argument sifatida oladi
- lambda -> bir qatorli anonim funksiya
- sorted() -> YANGI ro'yxat qaytaradi (asl o'zgarmaydi)
- list.sort() -> JOYIDA saralaydi, None qaytaradi
- key=... -> saralash mezonini belgilaydi
- filter() -> shartni bajaruvchi elementlarni qoldiradi
- map() -> har bir elementga funksiya qo'llaydi

MUHIM:
------
- filter() va map() "iterator" qaytaradi -> list() ga o'rash kerak
- sorted() asl ro'yxatni O'ZGARTIRMAYDI
- list.sort() asl ro'yxatni O'ZGARTIRADI va None qaytaradi
"""

# ============================================================
# TASK 1 — Funksiyalar qiymat sifatida
# ============================================================
# MAQSAD: Funksiya ham obyekt ekanligini tushunish.
#
# MANTIQ:
# - operation = square -> funksiya obyektini saqlaymiz
# - operation = square() -> funksiyani DARHOL chaqiradi (natijani saqlaydi)

print("\n===== TASK 1 =====")

def square(number):
    return number ** 2

operation = square           # QAVSSIZ! funksiya obyektini saqlaymiz
print(square(5))             # 25
print(operation(5))          # 25 - bir xil ishlaydi
print(operation is square)   # True - bir xil obyekt

# ============================================================
# TASK 2 — Funksiyani argument sifatida uzatish
# ============================================================
# MAQSAD: Yuqori tartibli funksiya (higher-order function).
#
# MANTIQ:
# - apply(operation, value) -> operation ni chaqiradi
# - operation - bu funksiya, uni QAVSSIZ uzatamiz

print("\n===== TASK 2 =====")

def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply(operation, value):
    return operation(value)   # operation ni chaqiramiz

print(apply(double, 5))       # 10
print(apply(triple, 5))       # 15

# ============================================================
# TASK 3 — Yuqori tartibli funksiya (transform)
# ============================================================
# MAQSAD: Har bir elementga funksiya qo'llash.
#
# MANTIQ:
# - Bo'sh ro'yxat yaratamiz
# - Har bir element uchun operation(value) chaqiramiz
# - Natijalarni qo'shamiz

print("\n===== TASK 3 =====")

def transform(values, operation):
    result = []
    for v in values:
        result.append(operation(v))
    return result

def square(number):
    return number ** 2

print(transform([1, 2, 3, 4], square))   # [1, 4, 9, 16]

# ============================================================
# TASK 4 — Lambda ifodalar
# ============================================================
# MAQSAD: Bir qatorli anonim funksiyalar.
#
# MANTIQ:
# - lambda parametrlar: ifoda
# - ifoda natijasi qaytariladi (return shart emas!)
# - lambda ni o'zgaruvchiga saqlash mumkin

print("\n===== TASK 4 =====")

double = lambda x: x * 2
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print(double(5))      # 10
print(add(3, 4))      # 7
print(is_even(8))     # True
print(is_even(7))     # False

# ============================================================
# TASK 5 — sorted() va list.sort() farqi
# ============================================================
# MAQSAD: Ikki saralash usuli orasidagi farqni tushunish.
#
# MANTIQ:
# - sorted(numbers) -> YANGI ro'yxat qaytaradi, asl o'zgarmaydi
# - numbers.sort() -> JOYIDA saralaydi, None qaytaradi

print("\n===== TASK 5 =====")

numbers = [8, 3, 10, 1, 6]

# A qism: sorted() -> yangi ro'yxat
ordered = sorted(numbers)
print("numbers:", numbers)     # [8, 3, 10, 1, 6] - o'zgarmadi
print("ordered:", ordered)     # [1, 3, 6, 8, 10]

# B qism: list.sort() -> joyida saralaydi
numbers.sort()
print("numbers (sort dan keyin):", numbers)   # [1, 3, 6, 8, 10]

result = numbers.sort()        # sort() None qaytaradi!
print("result:", result)       # None

# ============================================================
# TASK 6 — Teskari tartibda saralash
# ============================================================
# MAQSAD: reverse=True parametri.
#
# MANTIQ:
# - sorted(scores, reverse=True) -> kattadan kichikka
# - Asl ro'yxat o'zgarmaydi

print("\n===== TASK 6 =====")

scores = [82, 95, 73, 88, 61]
high_to_low = sorted(scores, reverse=True)
print("high_to_low:", high_to_low)   # [95, 88, 82, 73, 61]
print("scores:", scores)             # o'zgarmadi

# ============================================================
# TASK 7 — key bilan saralash
# ============================================================
# MAQSAD: key funksiyasi orqali saralash mezoni.
#
# MANTIQ:
# - key=len -> har bir so'zning uzunligi bo'yicha saralaydi
# - reverse=True -> teskari tartib

print("\n===== TASK 7 =====")

words = ["pear", "watermelon", "fig", "banana", "kiwi"]

shortest_first = sorted(words, key=len)
longest_first = sorted(words, key=len, reverse=True)

print("shortest_first:", shortest_first)   # ['fig', 'pear', 'kiwi', 'banana', 'watermelon']
print("longest_first:", longest_first)     # teskari

# ============================================================
# TASK 8 — Katta-kichik harflarga sezgir bo'lmagan saralash
# ============================================================
# MAQSAD: key=str.lower orqali registrga sezgir bo'lmagan saralash.
#
# MANTIQ:
# - str.lower -> harflarni kichik harflarga aylantiruvchi metod
# - key=str.lower -> barcha so'zlarni kichik harfga aylantirib saralaydi
# - Asl so'zlar o'zgartirilmaydi (faqat taqqoslashda ishlatiladi)

print("\n===== TASK 8 =====")

cities = ["berlin", "Algiers", "cairo", "Amsterdam", "zurich"]
ordered_cities = sorted(cities, key=str.lower)
print("ordered_cities:", ordered_cities)
# ['Algiers', 'Amsterdam', 'berlin', 'cairo', 'zurich']

# ============================================================
# TASK 9 — Lambda bilan tuplelarni saralash
# ============================================================
# MAQSAD: lambda orqali tuple elementiga murojaat.
#
# MANTIQ:
# - student[1] -> tuple ning ikkinchi elementi (ball)
# - reverse=True -> kattadan kichikka

print("\n===== TASK 9 =====")

students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]

sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("sorted_students:", sorted_students)
# [('Boris', 95), ('Mira', 88), ('Anna', 82), ('Daniel', 73)]

# ============================================================
# TASK 10 — filter() bilan filtrlash
# ============================================================
# MAQSAD: Shartni bajaruvchi elementlarni qoldirish.
#
# MANTIQ:
# - filter(funksiya, ketma-ketlik) -> iterator qaytaradi
# - list() ga o'rash kerak
# - lambda True qaytarsa -> element qoladi

print("\n===== TASK 10 =====")

scores = [45, 70, 82, 39, 91, 60, 58]
passing = list(filter(lambda s: s >= 60, scores))
print("passing:", passing)   # [70, 82, 91, 60]

# ============================================================
# TASK 11 — map() bilan o'zgartirish
# ============================================================
# MAQSAD: Har bir elementga funksiya qo'llash.
#
# MANTIQ:
# - map(funksiya, ketma-ketlik) -> iterator qaytaradi
# - lambda har bir narxni 1.1 ga ko'paytiradi (10% oshirish)

print("\n===== TASK 11 =====")

prices = [100, 250, 80, 40]
new_prices = list(map(lambda p: p * 1.1, prices))
print("new_prices:", new_prices)   # [110.0, 275.0, 88.0, 44.0]

# ============================================================
# TASK 12 — filter, sorted va map birgalikda
# ============================================================
# MAQSAD: Uchta am

#alni ketma-ket bajarish (pipeline).

# MANTIQ:
# 1. filter -> faqat o'tganlar
# 2. sorted -> ball bo'yicha kamayish tartibida
# 3. map -> faqat ismlarni olish

print("\n===== TASK 12 =====")

students = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
    {"name": "Daniel", "score": 67},
    {"name": "Sara", "score": 48}
]

# 1-qadam: faqat o'tganlar (score >= 60)
passing_students = list(filter(lambda s: s["score"] >= 60, students))

# 2-qadam: ball bo'yicha kamayish tartibida
sorted_students = sorted(passing_students, key=lambda s: s["score"], reverse=True)

# 3-qadam: faqat ismlar
names = list(map(lambda s: s["name"], sorted_students))

print("names:", names)   # ['Mira', 'Anna', 'Daniel']

# 