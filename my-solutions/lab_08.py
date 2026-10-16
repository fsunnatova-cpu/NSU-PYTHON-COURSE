"""
============================================================
NSU Python — Lab 08
Matnli fayllar bilan ishlash
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 14 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar
- Task 13-14: bonus

Fayl tuzilmasi:
    lab08.py            <- shu fayl
    data/               <- kirish fayllari
        note.txt
        names.txt
        scores.txt
        students.csv
    output/             <- chiqish fayllari (papka mavjud)

ASOSIY TUSHUNCHALAR:
--------------------
- Path (pathlib)     -> zamonaviy yo'l bilan ishlash
- with open(...)     -> faylni avtomatik yopadi
- Rejimlar (modes):
    "r" -> o'qish (read)
    "w" -> yozish (write) - mavjud faylni O'CHIRADI
    "a" -> qo'shish (append) - oxiriga qo'shadi
    "x" -> yaratish (exclusive) - mavjud bo'lsa xato
- read()        -> butun faylni o'qiydi
- readline()    -> bitta qatorni o'qiydi
- readlines()   -> barcha qatorlarni ro'yxat sifatida
- for line in f -> qatorma-qator o'qiydi (xotira tejaydi)
- write()       -> faylga yozadi (newline qo'shmaydi!)
- encoding="utf-8" -> matn kodirovkasi

XATOLARNI USHLASH:
------------------
- try/except FileNotFoundError -> fayl topilmasa
- try/except FileExistsError   -> "x" rejimida fayl mavjud bo'lsa
"""

from pathlib import Path
import re   # Task 14 uchun

# ============================================================
# YO'LLARNI SOZLASH
# ============================================================
# __file__ -> shu faylning yo'li
# .resolve() -> to'liq (absolute) yo'lga aylantiradi
# .parent -> ota papka
LAB_DIR = Path(__file__).resolve().parent
DATA = LAB_DIR / "data"
OUTPUT = LAB_DIR / "output"

# Papkalar mavjudligiga ishonch hosil qilamiz (xavfsizlik uchun)
DATA.mkdir(exist_ok=True)
OUTPUT.mkdir(exist_ok=True)

# ============================================================
# TASK 0 (yordamchi) — Test fayllarini yaratish
# ============================================================
# Agar sizda data/ fayllari bo'lmasa, quyidagi kod ularni yaratadi.
# O'chirib tashlashingiz mumkin, agar fayllar allaqachon mavjud bo'lsa.

def create_test_files():
    """Test uchun kerakli fayllarni yaratadi (agar mavjud bo'lmasa)."""
    
    note = DATA / "note.txt"
    if not note.exists():
        note.write_text(
            "Python is a great language.\n"
            "It has 3 main concepts.\n"
            "Version 3.12 is available.\n",
            encoding="utf-8"
        )
    
    names = DATA / "names.txt"
    if not names.exists():
        names.write_text(
            "Alice\n"
            "\n"
            "Bob\n"
            "Anna\n"
            "  Alex  \n"
            "Charlie\n",
            encoding="utf-8"
        )
    
    scores = DATA / "scores.txt"
    if not scores.exists():
        scores.write_text(
            "80\n"
            "75\n"
            "90\n"
            "85\n"
            "85\n",
            encoding="utf-8"
        )
    
    students = DATA / "students.csv"
    if not students.exists():
        students.write_text(
            "Anna,82\n"
            "Boris,55\n"
            "Mira,91\n"
            "Daniel,67\n",
            encoding="utf-8"
        )

create_test_files()

# ============================================================
# TASK 1 — Butun faylni o'qish
# ============================================================
# MAQSAD: with + read() bilan faylni o'qish.
#
# MANTIQ:
# - with open(...) -> faylni ochadi va blok tugagach avtomatik yopadi
# - "r" -> o'qish rejimi
# - encoding="utf-8" -> matn kodirovkasi
# - .read() -> butun faylni bitta satr sifatida qaytaradi
# - len(text) -> belgilar soni

print("\n===== TASK 1 =====")

note_path = DATA / "note.txt"

with open(note_path, "r", encoding="utf-8") as f:
    content = f.read()          # butun faylni o'qiymiz

print(content)                   # fayl mazmuni
print("Belgilar soni:", len(content))

# ============================================================
# TASK 2 — Ikki qatorni o'qish
# ============================================================
# MAQSAD: readline() bilan qatorma-qator o'qish.
#
# MANTIQ:
# - readline() -> har chaqiruvda bitta qator qaytaradi (oxirida \n bilan)
# - repr() -> satrni ko'rinadigan shaklda ko'rsatadi (\n ko'rinadi)

print("\n===== TASK 2 =====")

with open(note_path, "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()

print("line1:", repr(line1))   # 'Python is a great language.\n'
print("line2:", repr(line2))   # 'It has 3 main concepts.\n'

# ============================================================
# TASK 3 — Qatorlarni ro'yxatga o'qish
# ============================================================
# MAQSAD: readlines() bilan barcha qatorlarni olish.
#
# MANTIQ:
# - readlines() -> har bir qatorni element sifatida saqlaydigan ro'yxat
# - Har bir element oxirida \n bo'ladi
# - .strip() -> \n ni olib tashlaydi

print("\n===== TASK 3 =====")

names_path = DATA / "names.txt"

with open(names_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Qatorlar soni:", len(lines))

# Oxirgi qatorni \n siz chiqaramiz
last_name = lines[-1].strip()
print("Oxirgi ism:", last_name)

# ============================================================
# TASK 4 — Bo'sh bo'lmagan qatorlarni sanash
# ============================================================
# MAQSAD: Faylni qatorma-qator o'qish (xotira tejaydi).
#
# MANTIQ:
# - for line in f -> har bir qatorni ketma-ket o'qiydi
# - line.strip() -> bo'shliq va \n ni olib tashlaydi
# - Agar natija bo'sh bo'lmasa -> sanaymiz

print("\n===== TASK 4 =====")

count = 0

with open(names_path, "r", encoding="utf-8") as f:
    for line in f:                    # qatorma-qator
        if line.strip():              # bo'sh emasmi?
            count += 1

print("Bo'sh bo'lmagan qatorlar:", count)

# ============================================================
# TASK 5 — Hisobot yozish
# ============================================================
# MAQSAD: "w" rejimida faylga yozish.
#
# MANTIQ:
# - "w" -> faylni YANGI qilib yozadi (mavjud bo'lsa O'CHIRADI!)
# - write() -> newline AVTOMATIK qo'shilmaydi, qo'lda \n kerak

print("\n===== TASK 5 =====")

report_path = OUTPUT / "name_report.txt"
count = 0

with open(names_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            count += 1

with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"Names: {count}\n")   # \n qo'lda qo'shamiz

print(f"Yozildi: {report_path}")

# ============================================================
# TASK 6 — Log yozuvini qo'shish
# ============================================================
# MAQSAD: "a" rejimida faylga qo'shish.
#
# MANTIQ:
# - "a" -> fayl oxiriga qo'shadi (mavjud mazmun saqlanadi)
# - Har safar ishga tushirilganda yangi yozuv qo'shiladi

print("\n===== TASK 6 =====")

log_path = OUTPUT / "activity.log"

with open(log_path, "a", encoding="utf-8") as f:
    f.write("Lab 08 completed\n")

print(f"Log yozuvi qo'shildi: {log_path}")

# ============================================================
# TASK 7 — Ustidan yozmasdan yaratish
# ============================================================
# MAQSAD: "x" rejimi + FileExistsError.
#
# MANTIQ:
# - "x" -> fayl mavjud bo'lmasa yaratadi
# - Agar fayl mavjud bo'lsa -> FileExistsError
# - try/except bilan xatoni ushlaymiz

print("\n===== TASK 7 =====")

first_run_path = OUTPUT / "first_run.txt"

try:
    with open(first_run_path, "x", encoding="utf-8") as f:
        f.write("First run")
    print("Fayl yaratildi:", first_run_path)
except FileExistsError:
    print(f"Fayl allaqachon mavjud: {first_run_path}")

# ============================================================
# TASK 8 — Yo'q faylni boshqarish
# ============================================================
# MAQSAD: FileNotFoundError ni ushlash.
#
# MANTIQ:
# - Mavjud bo'lmagan faylni ochishga harakat qilamiz
# - FileNotFoundError yuzaga keladi
# - Uni try/except bilan ushlaymiz

print("\n===== TASK 8 =====")

missing_path = DATA / "missing.txt"

try:
    with open(missing_path, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("Input file not found")

# ============================================================
# TASK 9 — Ismlarni filtrlash va yangi faylga yozish
# ============================================================
# MAQSAD: O'qish va yozishni birgalikda qilish.
#
# MANTIQ:
# - Har bir qatorni o'qib, "A" yoki "a" bilan boshlanadiganini yozamiz
# - .strip() -> bo'shliq va \n ni olib tashlaydi

print("\n===== TASK 9 =====")

a_names_path = OUTPUT / "a_names.txt"

with open(names_path, "r", encoding="utf-8") as fin, \
     open(a_names_path, "w", encoding="utf-8") as fout:
    
    for line in fin:
        name = line.strip()
        if name and (name.startswith("A") or name.startswith("a")):
            fout.write(name + "\n")

print(f"Yozildi: {a_names_path}")

# ============================================================
# TASK 10 — Fayldan o'rtacha hisoblash
# ============================================================
# MAQSAD: Raqamlarni o'qib, o'rtacha hisoblash.
#
# MANTIQ:
# - Har bir qatorni int() ga o'giramiz
# - Bo'sh ro'yxat holatini ham hisobga olamiz (0 ga bo'lish!)

print("\n===== TASK 10 =====")

scores_path = DATA / "scores.txt"
average_path = OUTPUT / "average.txt"

scores = []

with open(scores_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:                      # bo'sh emasmi?
            scores.append(int(line))

if len(scores) == 0:
    avg = 0
    result = "Average: no scores"
else:
    avg = sum(scores) / len(scores)
    result = f"Average: {avg:.1f}"

with open(average_path, "w", encoding="utf-8") as f:
    f.write(result + "\n")

print(f"Natija: {result}")

# ============================================================
# TASK 11 — Oddiy jadvalni o'qish
# ============================================================
# MAQSAD: CSV faylini o'qish (vergul bilan ajratilgan).
#
# MANTIQ:
# - line.split(",") -> 2 ta bo'lak: [ism, ball]
# - int(ball) -> butun songa aylantiramiz
# - Ball >= 80 bo'lsa -> chiqaramiz

print("\n===== TASK 11 =====")

students_path = DATA / "students.csv"

with open(students_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue                  # bo'sh qatorlarni o'tkazamiz
        
        parts = line.split(",")
        name = parts[0].strip()
        score = int(parts[1].strip())
        
        if score >= 80:
            print(f"{name}: {score}")

# ============================================================
# TASK 12 — So'zlar sonini saqlash
# ============================================================
# MAQSAD: split() bilan so'zlarni sanash va faylga yozish.
#
# MANTIQ:
# - text.split() -> bo'shliqlar bo'yicha bo'laklarga ajratadi
# - len(words) -> so'zlar soni

print("\n===== TASK 12 =====")

word_count_path = OUTPUT / "word_count.txt"

with open(note_path, "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
word_count = len(words)

with open(word_count_path, "w", encoding="utf-8") as f:
    f.write(f"Words: {word_count}\n")

print(f"So'zlar soni: {word_count}")

# 