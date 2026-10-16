"""
============================================================
NSU Python — Lab 09
Istisnolar (Exceptions) va OOP asoslari
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 14 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar (kurs minimumi: kamida 10 ta)
- Task 13-14: bonus

ASOSIY TUSHUNCHALAR:
--------------------
ISTISNOLAR (EXCEPTIONS):
- try/except        -> xatolarni ushlash
- try/except/else   -> else xato bo'lmaganda ishlaydi
- try/except/finally-> finally HAR DOIM ishlaydi
- raise             -> o'zimiz xato ko'taramiz
- ValueError        -> noto'g'ri qiymat
- ZeroDivisionError -> 0 ga bo'lish
- FileNotFoundError -> fayl topilmadi
- FileExistsError   -> fayl allaqachon mavjud

OOP (Object-Oriented Programming):
- class            -> sinf e'lon qiladi
- __init__         -> konstruktor (obyekt yaratilganda ishlaydi)
- self             -> obyektning o'ziga havola
- Instance attribute -> self.name kabi o'zgaruvchilar
- Method           -> sinf ichidagi funksiya (self bilan)
- Obyekt           -> sinfdan yaratilgan nusxa

MUHIM QOIDALAR:
---------------
- try/except/else/finally tartibi:
    try:     xato bo'lishi mumkin bo'lgan kod
    except:  xato bo'lsa ishlaydi
    else:    xato bo'lmasa ishlaydi
    finally: HAR DOIM ishlaydi
- raise bilan xato ko'tarish mumkin
- __init__ ichida instance attribute yaratish yaxshi odat
- self.scores = [] -> HAR BIR obyekt uchun yangi ro'yxat
- Sinf atributi (class attribute) BARCHA obyektlar uchun umumiy
"""

from pathlib import Path

# ============================================================
# YO'LLARNI SOZLASH
# ============================================================
LAB_DIR = Path(__file__).resolve().parent
DATA = LAB_DIR / "data"

# Papka mavjudligiga ishonch hosil qilamiz
DATA.mkdir(exist_ok=True)

# ============================================================
# TASK 0 (yordamchi) — Test fayllarini yaratish
# ============================================================
# Sizda fayllar bo'lmasa, quyidagi kod ularni yaratadi.

def create_test_files():
    """Test uchun kerakli fayllarni yaratadi."""
    
    valid = DATA / "number_valid.txt"
    if not valid.exists():
        valid.write_text("42\n", encoding="utf-8")
    
    invalid = DATA / "number_invalid.txt"
    if not invalid.exists():
        invalid.write_text("hello\n", encoding="utf-8")
    
    mixed = DATA / "mixed_scores.txt"
    if not mixed.exists():
        mixed.write_text(
            "80\n"
            "bad\n"
            "100\n"
            "105\n"
            "60\n"
            "-2\n",
            encoding="utf-8"
        )
    
    students = DATA / "student_scores.txt"
    if not students.exists():
        students.write_text(
            "Anna,80\n"
            "Anna,bad\n"
            "Anna,90\n"
            "Omar,70\n"
            "Omar,101\n",
            encoding="utf-8"
        )

create_test_files()

# ============================================================
# TASK 1 — Xavfsiz butun songa aylantirish
# ============================================================
# MAQSAD: try/except/else bilan ValueError ni ushlash.
#
# MANTIQ:
# - try: int() ga aylantirishga harakat qilamiz
# - except ValueError: xato bo'lsa ishlaydi
# - else: xato bo'lmasa ishlaydi (faqat try muvaffaqiyatli bo'lganda)

print("\n===== TASK 1 =====")

text = input("Butun son kiriting: ")

try:
    number = int(text)       # xato bo'lishi mumkin
except ValueError:
    # int("hello") yoki int("3.5") -> ValueError
    print("Invalid integer")
else:
    # Bu blok faqat xato BO'LMAGANDA ishlaydi
    print(f"Number: {number}")

# ============================================================
# TASK 2 — Xavfsiz bo'lish
# ============================================================
# MAQSAD: Ikki xil xatoni alohida ushlash.
#
# MANTIQ:
# - ValueError     -> noto'g'ri matn
# - ZeroDivisionError -> 0 ga bo'lish
# - Har biri uchun ALOHIDA except bloki
print("\n===== TASK 2 =====")

try:
    a = int(input("Birinchi son: "))
    b = int(input("Ikkinchi son: "))
    result = a / b              # 0 ga bo'lish mumkin
except ValueError:
    print("Enter integers")     # matn kiritildi
except ZeroDivisionError:
    print("Cannot divide by zero")  # b = 0
else:
    print(f"Result: {result}")  # muvaffaqiyat

# ============================================================
# TASK 3 — try, except, else, finally
# ============================================================
# MAQSAD: To'rt blokni birgalikda ko'rish.
#
# MANTIQ:
# - try:     int(text) - xato bo'lishi mumkin
# - except:  xato bo'lsa ishlaydi
# - else:    xato bo'lmasa ishlaydi
# - finally: HAR DOIM ishlaydi (xato bo'lsa ham, bo'lmasa ham)

print("\n===== TASK 3 =====")

for text in ["8", "bad", "0"]:
    try:
        number = int(text)
    except ValueError:
        print(f"Invalid: {text}")
    else:
        print(f"Converted: {number}")
    finally:
        # Bu blok har doim ishlaydi
        print("Attempt finished")

# ============================================================
# TASK 4 — raise bilan ballni tekshirish
# ============================================================
# MAQSAD: O'zimiz xato ko'tarish (raise).
#
# MANTIQ:
# - 0 <= score <= 100 -> qaytaramiz
# - Aks holda -> ValueError ko'taramiz
# - Chaqiruvchi tomonda try/except bilan ushlaymiz

print("\n===== TASK 4 =====")

def validate_score(score):
    if 0 <= score <= 100:
        return score
    # raise -> xato ko'taradi
    raise ValueError("Score must be between 0 and 100")

for s in [-1, 0, 75, 100, 101]:
    try:
        result = validate_score(s)
        print(result)
    except ValueError as e:
        print(e)              # xato xabari

# ============================================================
# TASK 5 — Faylni xavfsiz o'qish
# ============================================================
# MAQSAD: Funksiya ichida xatoni USHLAMASLIK, chaqiruvchi tomonda ushlash.
#
# MANTIQ:
# - Funksiya ichida xatolarni "propagate" qilamiz (o'tkazamiz)
# - Chaqiruvchi tomonda try/except bilan ushlaymiz
# - Bu yaxshi dizayn - funksiya "toza" qoladi

print("\n===== TASK 5 =====")

def read_first_integer(path):
    # with -> faylni avtomatik yopadi
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline().strip()   # birinchi qator
        return int(line)              # int() xato berishi mumkin
    # Bu funksiyada xatolarni USHLAMAYMIZ - ular tashqariga o'tadi

# Chaqiruvchi tomon
for filename in ["number_valid.txt", "number_invalid.txt", "missing.txt"]:
    path = DATA / filename
    try:
        value = read_first_integer(path)
        print(f"Number: {value}")
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid file content")

# ============================================================
# TASK 6 — To'g'ri kiritilguncha qayta so'rash
# ============================================================
# MAQSAD: while True + try/except bilan validatsiya.
#
# MANTIQ:
# - while True -> to'g'ri kiritilguncha davom etadi
# - ValueError -> matn kiritildi
# - n <= 0 -> musbat emas
# - Aks holda -> break

print("\n===== TASK 6 =====")

while True:
    text = input("Musbat butun son kiriting: ")
    
    try:
        n = int(text)
    except ValueError:
        print("Enter a whole number")
        continue                    # qaytadan so'raymiz
    
    if n <= 0:
        print("Enter a positive number")
        continue                    # qaytadan so'raymiz
    
    print(f"Accepted: {n}")
    break                           # muvaffaqiyat

# ============================================================
# TASK 7 — Book sinfi
# ============================================================
# MAQSAD: Birinchi sinfni yaratish.
#
# MANTIQ:
# - class Book: -> sinf e'lon qiladi
# - __init__ -> konstruktor (obyekt yaratilganda ishlaydi)
# - self -> obyektning o'zi
# - self.title -> instance attribute (har bir obyekt uchun alohida)

print("\n===== TASK 7 =====")

class Book:
    def __init__(self, title, author):
        # Instance attribute lar
        self.title = title
        self.author = author
    
    def describe(self):
        # RETURN qiladi, print emas!
        return f"{self.title} by {self.author}"

# Ikki xil kitob yaratamiz
book1 = Book("Python Basics", "A. Ivanov")
book2 = Book("Data Science", "B. Petrov")

print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)
print(book1.describe())     # Python Basics by A. Ivanov
print(book2.describe())     # Data Science by B. Petrov

# ============================================================
# TASK 8 — Rectangle sinfi
# ============================================================
# MAQSAD: Hisoblash metodlari bilan sinf.
#
# MANTIQ:
# - width, height -> instance attribute
# - area() -> width * height
# - perimeter() -> 2 * (width + height)

print("\n===== TASK 8 =====")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(3, 4)
rect2 = Rectangle(2, 5)

print(f"Rectangle(3, 4): area={rect1.area()}, perimeter={rect1.perimeter()}")
print(f"Rectangle(2, 5): area={rect2.area()}, perimeter={rect2.perimeter()}")

# ============================================================
# TASK 9 — Counter sinfi
# ============================================================
# MAQSAD: Sukut argument + holat (state) saqlash.
#
# MANTIQ:
# - start=0 -> sukut qiymat
# - self.value -> joriy qiymat
# - add() -> qiymatni oshiradi
# - reset() -> 0 ga qaytaradi
# - get_value() -> qiymatni qaytaradi

print("\n===== TASK 9 =====")

class Counter:
    def __init__(self, start=0):
        self.value = start
    
    def add(self, amount):
        self.value += amount
    
    def reset(self):
        self.value = 0
    
    def get_value(self):
        return self.value

c = Counter(10)
c.add(3)
c.add(-2)
print("Counter(10) + 3 - 2 =", c.get_value())   # 11

c.reset()
print("reset dan keyin:", c.get_value())        # 0

c2 = Counter()
print("Counter() boshlang'ich:", c2.get_value())  # 0

# ============================================================
# TASK 10 — Mustaqil Student obyektlari
# ============================================================
# MAQSAD: Instance attribute har bir obyekt uchun ALOHIDA ekanligini
#         ko'rsatish.
#
# MANTIQ:
# - self.scores = [] -> __init__ ICHIDA yaratilishi SHART
# - Agar class darajasida yaratilsa -> BARCHA obyektlar uchun umumiy bo'ladi
# - __init__ ichida yaratilsa -> har bir obyekt uchun yangi ro'yxat

print("\n===== TASK 10 =====")

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []        # HAR BIR obyekt uchun YANGI ro'yxat!
    
    def add_score(self, score):
        self.scores.append(score)

anna = Student("Anna")
omar = Student("Omar")

anna.add_score(80)
anna.add_score(90)
# Omar ga hech narsa qo'shmaymiz

print("Anna:", anna.scores)     # [80, 90]
print("Omar:", omar.scores)     # [] - BO'SH!

# NEGA? Chunki self.scores = [] HAR BIR obyekt uchun alohida ro'yxat
# yaratadi. Agar class darajasida scores = [] yozilsa, u umumiy bo'lardi.

# ============================================================
# TASK 11 — Validatsiyali Student sinfi
# ============================================================
# MAQSAD: Metod ichida raise bilan validatsiya.
#
# MANTIQ:
# - add_score() ichida tekshiramiz
# - Noto'g'ri bo'lsa -> raise ValueError
# - Ro'yxatga FAQAT to'g'ri qiymat qo'shiladi

print("\n===== TASK 11 =====")

class ValidatedStudent:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, score):
        if score < 0 or score > 100:
            # Ro'yxatga QO'SHISHDAN OLDIN xato ko'taramiz
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(score)

anna = ValidatedStudent("Anna")

for score in [80, -1, 100, 101]:
    try:
        anna.add_score(score)
    except ValueError:
        print(f"Rejected: {score}")

print("Scores:", anna.scores)   # [80, 100]

# ============================================================
# TASK 12 — O'rtacha va bo'sh ma'lumot
# ============================================================
# MAQSAD: Bo'sh ro'yxat uchun xato ko'tarish.
#
# MANTIQ:
# - average() -> bo'sh bo'lsa raise ValueError
# - 0 qaytarish YARAMAYDI (0 haqiqiy o'rtacha bo'lishi mumkin)

print("\n===== TASK 12 =====")

class StudentReport:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(score)
    
    def average(self):
        if len(self.scores) == 0:
            raise ValueError("No scores recorded")
        return sum(self.scores) / len(self.scores)

anna = StudentReport("Anna")
anna.add_score(80)
anna.add_score(90)
print(f"Anna average: {anna.average()}")   # 85.0

omar = StudentReport("Omar")
try:
    print(omar.average())
except ValueError as e:
    print(e)                                # No scores recorded

#