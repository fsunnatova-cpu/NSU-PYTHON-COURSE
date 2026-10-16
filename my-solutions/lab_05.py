"""
============================================================
NSU Python — Lab 05
Funksiyalar amalda: argumentlar, rekursiya, math, list metodlari
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 38 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar
- Task 13-14: bonus
- Task 15-38: qo'shimcha mashqlar

TAQIQLANGAN NARSALAR (bu labda ishlatilmaydi):
---------------------------------------------
- lambda
- sorted()
- filter()
- map()

MUHIM TUSHUNCHALAR:
-------------------
- *args   -> istalgan sonda pozitsion argumentlarni qabul qiladi (tuple)
- **kwargs-> istalgan sonda kalit-so'z argumentlarini qabul qiladi (dict)
- def     -> funksiya e'lon qiladi
- return  -> qiymat qaytaradi (return yo'q bo'lsa -> None)
- scope   -> o'zgaruvchi ko'rinish doirasi (global / local)
- rekursiya-> funksiya o'zini-o'zi chaqiradi
- math    -> matematik funksiyalar moduli
"""

import math   # Task 12, 19, 31, 38 uchun kerak

# ============================================================
# TASK 1 — Pozitsion va kalit-so'z argumentlar
# ============================================================
# MAQSAD: Funksiyani turli usullar bilan chaqirishni o'rganish.
#
# MANTIQ:
# - Pozitsion argumentlar -> tartib bo'yicha joylashadi
# - Kalit-so'z argumentlari -> nom bo'yicha, tartib muhim emas
# - Aralash -> avval pozitsion, keyin kalit-so'z

print("\n===== TASK 1 =====")

def describe_student(name, age, city):
    # Uchta parametr: name, age, city
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# 1) Faqat pozitsion argumentlar (tartib muhim)
describe_student("Anna", 23, "Novosibirsk")

# 2) Faqat kalit-so'z argumentlari (tartib muhim emas)
describe_student(city="Moscow", name="Ivan", age=20)

# 3) Bitta pozitsion + qolganlari kalit-so'z
describe_student("Mira", city="Kazan", age=21)

# ============================================================
# TASK 2 — Default (sukut bo'yicha) argumentlar
# ============================================================
# MAQSAD: Argumentga sukut qiymat berish.
#
# MANTIQ:
# - rate=2.5 -> agar rate berilmasa, 2.5 ishlatiladi
# - Sukut argumentlar funksiya e'lonida OXIRIDA bo'lishi kerak

print("\n===== TASK 2 =====")

def shipping_cost(weight, rate=2.5):
    return weight * rate

print(shipping_cost(4))              # 10.0 (rate = 2.5)
print(shipping_cost(4, 3.0))         # 12.0 (rate = 3.0)
print(shipping_cost(4, rate=1.5))    # 6.0  (kalit-so'z bilan)

# ============================================================
# TASK 3 — Erta return (early return)
# ============================================================
# MAQSAD: Xatolikni darhol aniqlab, funksiyadan chiqish.
#
# MANTIQ:
# - b == 0 -> None qaytaramiz (0 ga bo'lish mumkin emas)
# - Aks holda -> a / b

print("\n===== TASK 3 =====")

def safe_divide(a, b):
    if b == 0:
        return None          # erta chiqish
    return a / b

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None

# ============================================================
# TASK 4 — *args: umumiy ball
# ============================================================
# MAQSAD: Istalgan sonda argumentlarni qabul qilish.
#
# MANTIQ:
# - *scores -> barcha pozitsion argumentlar bitta TUPLEDA yig'iladi
# - Bo'sh bo'lsa ham ishlaydi (sum = 0)

print("\n===== TASK 4 =====")

def total_score(*scores):
    total = 0
    for s in scores:         # scores - bu tuple
        total += s
    return total

print(total_score(10, 20, 30))   # 60
print(total_score(5))            # 5
print(total_score())             # 0

# ============================================================
# TASK 5 — *args: o'rtacha ball
# ============================================================
# MAQSAD: Bo'sh bo'lsa None, aks holda o'rtacha.
#
# MANTIQ:
# - len(scores) -> tuple uzunligi
# - Bo'sh bo'lsa -> None

print("\n===== TASK 5 =====")

def average_score(*scores):
    if len(scores) == 0:
        return None
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

print(average_score(80, 90, 100))   # 90.0
print(average_score())              # None

# ============================================================
# TASK 6 — **kwargs: profil
# ============================================================
# MAQSAD: Kalit-so'z argumentlarini dict sifatida qabul qilish.
#
# MANTIQ:
# - **details -> barcha kalit=qiymat juftlari dictga yig'iladi
# - .items() -> kalit va qiymat juftlarini beradi

print("\n===== TASK 6 =====")

def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Anna", city="Novosibirsk", year=1)

# ============================================================
# TASK 7 — Fixed + *args + **kwargs birgalikda
# ============================================================
# MAQSAD: Uch xil argument turini birlashtirish.
#
# TARTIB MUHIM: fixed -> *args -> **kwargs

print("\n===== TASK 7 =====")

def course_report(student, *scores, **options):
    print("Student:", student)
    print("Scores:", scores)        # tuple
    print("Options:", options)      # dict

course_report(
    "Mira",
    80, 92, 75,
    rounded=True,
    scale=100
)

# ============================================================
# TASK 8 — Scope (ko'rinish doirasi)
# ============================================================
# MAQSAD: Global va local o'zgaruvchilar farqini tushunish.
#
# MANTIQ:
# - TAX_RATE -> global (fayl darajasida)
# - tax -> local (faqat funksiya ichida mavjud)
# - Global o'zgaruvchini funksiya ichida O'QISH mumkin

print("\n===== TASK 8 =====")

TAX_RATE = 0.20     # global o'zgaruvchi

def final_price(price):
    tax = price * TAX_RATE   # TAX_RATE - global, tax - local
    return price + tax

print(final_price(100))      # 120.0
# print(tax)                 # XATO! tax faqat funksiya ichida mavjud

# ============================================================
# TASK 9 — Rekursiv sanoq (countdown)
# ============================================================
# MAQSAD: Rekursiyani birinchi marta ko'rish.
#
# MANTIQ:
# - Base case (asosiy holat): n == 0 -> "Go!" va to'xtash
# - Recursive case: n > 0 -> n chiqaramiz va countdown(n-1) chaqiramiz
#
# MUHIM: tsikl ISHLATILMAYDI!

print("\n===== TASK 9 =====")

def countdown(n):
    if n == 0:
        print("Go!")            # base case
        return                  # funksiyadan chiqamiz
    print(n)                    # hozirgi qiymat
    countdown(n - 1)            # rekursiv chaqiruv

countdown(3)

# ============================================================
# TASK 10 — Rekursiv faktorial
# ============================================================
# MAQSAD: n! ni rekursiya bilan hisoblash.
#
# MANTIQ:
# - n < 0 -> None (xato)
# - n == 0 -> 1 (base case: 0! = 1)
# - n > 0 -> n * factorial(n-1)

print("\n===== TASK 10 =====")

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1                       # base case
    return n * factorial(n - 1)        # rekursiv qadam

print(factorial(5))    # 120
print(factorial(0))    # 1
print(factorial(-2))   # None

# ============================================================
# TASK 11 — Rekursiv yig'indi
# ============================================================
# MAQSAD: 1 + 2 + ... + n ni rekursiya bilan.
#
# MANTIQ:
# - n < 0 -> None
# - n == 0 -> 0 (base case)
# - n > 0 -> n + sum_to(n-1)

print("\n===== TASK 11 =====")

def sum_to(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_to(n - 1)

print(sum_to(4))    # 10
print(sum_to(0))    # 0

# ============================================================
# TASK 12 — math moduli va list metodlari
# ============================================================
# MAQSAD: math.pi, math.ceil, math.floor va list metodlarini o'rganish.

print("\n===== TASK 12 — A qism (math) =====")

# radius ni so'raymiz
radius = float(input("Aylana radiusi: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Circumference:", circumference)
print("Area:", area)
print("Area ceil:", math.ceil(area))     # yuqoriga yaxlitlaydi
print("Area floor:", math.floor(area))   # pastga yaxlitlaydi

print("\n===== TASK 12 — B qism (list metodlari) =====")

numbers = [10, 20, 20, 30]

numbers.append(40)              # oxiriga qo'shadi
numbers.extend([50, 60])        # ro'yxatni kengaytiradi
numbers.insert(1, 15)           # 1-indeksga 15 qo'yadi
print("20 soni necha marta:", numbers.count(20))
print("Birinchi 30 indeksi:", numbers.index(30))
numbers.remove(20)              # birinchi 20 ni o'chiradi
removed = numbers.pop()         # oxirgi elementni oladi va o'chiradi
print("numbers:", numbers)
print("removed:", removed)

# ============================================================
# BONUS TASK 13 — Rekursiv raqamlar yig'indisi
# ============================================================
# MAQSAD: Sondagi barcha raqamlar yig'indisini rekursiya bilan.
#
# MANTIQ:
# - n < 10 -> n (bir xonali son)
# - aks holda -> (n % 10) + digit_sum(n // 10)
#
# n % 10 -> oxirgi raqam
# n // 10 -> oxirgi raqam olib tashlangan son

print("\n===== BONUS TASK 13 =====")

def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)

print(digit_sum(1234))   # 10
print(digit_sum(7))      # 7

# ============================================================
# BONUS TASK 14 — Talaba natijalari xulosasi
# ============================================================
# MAQSAD: *args + **kwargs + shartlar birgalikda.
#
# MANTIQ:
# - scores bo'sh -> "No scores"
# - average -> o'rtacha
# - passed -> passing dan katta yoki teng ballar soni

print("\n===== BONUS TASK 14 =====")

def result_summary(name, *scores, passing=60):
    if len(scores) == 0:
        return "No scores"
    
    total = 0
    passed = 0
    for s in scores:
        total += s
        if s >= passing:
            passed += 1
    
    avg = total / len(scores)
    return f"{name}: average={avg}, passed={passed}/{len(scores)}"

print(result_summary("Anna", 80, 70, 50, 120, passing=60))

# 