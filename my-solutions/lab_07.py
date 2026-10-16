"""
============================================================
NSU Python — Lab 07
Satrlar (strings) va muntazam ifodalar (regular expressions)
============================================================

BU FAYL NIMA QILADI?
--------------------
Bu faylda 14 ta topshiriq ketma-ket yechilgan:
- Task 1-12: asosiy topshiriqlar
- Task 13-14: bonus

ASOSIY TUSHUNCHALAR:
--------------------
Satr metodlari:
- strip()      -> bosh va oxirdagi bo'shliqlarni olib tashlaydi
- lower()      -> kichik harflarga aylantiradi
- upper()      -> katta harflarga aylantiradi
- title()      -> har so'zning birinchi harfini katta qiladi
- split()      -> bo'shliq yoki belgi bo'yicha bo'laklarga ajratadi
- join()       -> ro'yxatni bitta satrga birlashtiradi
- count()      -> substring necha marta uchrashini sanaydi
- find()       -> substring indeksini qaytaradi (topilmasa -1)
- startswith() -> boshlanishini tekshiradi
- endswith()   -> tugashini tekshiradi

Regex (muntazam ifodalar) — re moduli:
- re.findall()    -> barcha mos keluvchi qismlarni topadi
- re.search()     -> istalgan joydan qidiradi
- re.match()      -> faqat BOSHIDAN qidiradi
- re.fullmatch()  -> butun satr mos kelishi kerak

Regex belgilari:
- [0-9]  -> istalgan raqam
- [A-Z]  -> istalgan katta harf
- [A-Za-z] -> istalgan harf
- +      -> bir yoki ko'p marta
- *      -> nol yoki ko'p marta
- ?      -> nol yoki bir marta (ixtiyoriy)
- \\d     -> raqam ([0-9] bilan bir xil)
- {4}    -> aniq 4 marta

MUHIM:
------
- Satrlar O'ZGARMAS (immutable) -> metodlar YANGI satr qaytaradi
- Raw string: r"..." -> backslash maxsus belgi emas
"""

import re   # Task 7-14 uchun kerak

# ============================================================
# TASK 1 — Talaba ismini tozalash
# ============================================================
# MAQSAD: strip() va title() bilan ismni tozalash.
#
# MANTIQ:
# - raw.strip()  -> bosh va oxirdagi bo'shliqlarni olib tashlaydi
# - .title()     -> har so'zning birinchi harfini katta qiladi,
#                   qolganlarini kichik qiladi
#
# MUHIM: Satrlar O'ZGARMAS (immutable). Shuning uchun raw ning
# o'zi o'zgarmaydi, faqat yangi satr qaytariladi.

print("\n===== TASK 1 =====")

raw = "  aLiCe SMITH  "
clean = raw.strip().title()   # yangi satr yaratamiz
print(clean)                   # Alice Smith

# NEGA raw O'ZGARMAYDI?
# Chunki Python'da satrlar immutable (o'zgarmas). strip() va title()
# ASL satrni o'zgartirmaydi, balki YANGI satr qaytaradi.
print("raw hali ham:", repr(raw))   # '  aLiCe SMITH  '

# ============================================================
# TASK 2 — Fayl kengaytmasini olish
# ============================================================
# MAQSAD: Oxirgi nuqtadan keyingi qismni olish.
#
# MANTIQ:
# - filename.split(".") -> ro'yxatga ajratadi
# - [-1] -> oxirgi elementni oladi

print("\n===== TASK 2 =====")

filename = "final.report.pdf"
extension = filename.split(".")[-1]
print(extension)   # pdf

filename2 = "notes.txt"
print(filename2.split(".")[-1])   # txt

# ============================================================
# TASK 3 — So'zlarni ajratish va birlashtirish
# ============================================================
# MAQSAD: split() va join() birgalikda.
#
# MANTIQ:
# - text.split() -> bo'shliq bo'yicha ajratadi (ketma-ket bo'shliqlarni
#                  avtomatik birlashtiradi)
# - " ".join(words) -> ro'yxatni bitta bo'shliq bilan birlashtiradi

print("\n===== TASK 3 =====")

text = "  Python   files  are useful  "
words = text.split()               # bo'shliqlar bo'yicha ajratadi
print("words:", words)             # ['Python', 'files', 'are', 'useful']

clean = " ".join(words)
print("clean:", clean)             # Python files are useful

# ============================================================
# TASK 4 — Substringni sanash
# ============================================================
# MAQSAD: count(), startswith(), endswith().
#
# MANTIQ:
# - count("ana") -> bir-biriga to'g'ri kelmaydigan mosliklarni sanaydi
# - "banana bandana" da: ba[A]na[na]... -> "ana" 2 marta
#   (banana -> 1 marta, bandana -> 1 marta)

print("\n===== TASK 4 =====")

text = "banana bandana"
print("count('ana'):", text.count("ana"))         # 2
print("startswith('ban'):", text.startswith("ban"))  # True
print("endswith('ana'):", text.endswith("ana"))      # True

# MUHIM: count() bir-biriga to'g'ri kelmaydigan mosliklarni sanaydi.
# "banana" da "ana" faqat 1 marta sanaladi (ban[ana]na),
# chunki keyingi "ana" oldingisi bilan kesishadi.

# ============================================================
# TASK 5 — Ixtiyoriy ajratuvchi
# ============================================================
# MAQSAD: find() -1 tekshiruvi.
#
# MANTIQ:
# - find("-") -> indeks qaytaradi yoki -1 (topilmasa)
# - Agar -1 bo'lsa -> butun qiymatni qaytaramiz
# - Aks holda -> "-" dan oldingi qismni qaytaramiz

print("\n===== TASK 5 =====")

def split_code(value):
    pos = value.find("-")          # "-" indeksini qidiramiz
    if pos == -1:
        return value               # topilmadi -> butun qiymat
    return value[:pos]             # "-" dan oldingi qism

print(split_code("NS-205"))   # NS
print(split_code("NS205"))    # NS205

# ============================================================
# TASK 6 — Oddiy yozuvni normallashtirish
# ============================================================
# MAQSAD: split(",") + strip() har bir bo'lakda.
#
# MANTIQ:
# - row.split(",") -> vergul bo'yicha bo'laklarga ajratadi
# - Har bir bo'lakni strip() qilamiz
# - " | ".join(...) -> birlashtiramiz

print("\n===== TASK 6 =====")

row = "  Anna , 82 , NSU  "
parts = row.split(",")                    # ['  Anna ', ' 82 ', ' NSU  ']
cleaned = [p.strip() for p in parts]      # list comprehension
result = " | ".join(cleaned)
print(result)                             # Anna | 82 | NSU

# ============================================================
# TASK 7 — Matndan raqamlarni topish
# ============================================================
# MAQSAD: re.findall() bilan raqamlarni olish.
#
# MANTIQ:
# - r"[0-9]+" -> bir yoki ko'p raqam
# - findall() -> barcha mos keluvchi qismlarni ro'yxat sifatida qaytaradi
# - [int(s) for s in ...] -> satrlarni butun sonlarga aylantiramiz

print("\n===== TASK 7 =====")

text = "Rooms B-204, C-17, A-315"
digit_strings = re.findall(r"[0-9]+", text)
print("digit_strings:", digit_strings)      # ['204', '17', '315']

digits = [int(s) for s in digit_strings]
print("digits:", digits)                    # [204, 17, 315]

# ============================================================
# TASK 8 — Talaba ID sini tekshirish
# ============================================================
# MAQSAD: re.fullmatch() bilan butun satrni tekshirish.
#
# MANTIQ:
# - [A-Z]{2}   -> aniq 2 ta katta harf
# - -          -> chiziqcha
# - [0-9]{4}   -> aniq 4 ta raqam
# - fullmatch  -> butun satr mos kelishi SHART

print("\n===== TASK 8 =====")

def is_valid_id(value):
    # r"..." -> raw string (backslash maxsus emas)
    # fullmatch -> butun satrni tekshiradi
    pattern = r"[A-Z]{2}-[0-9]{4}"
    return re.fullmatch(pattern, value) is not None

print(is_valid_id("AB-2047"))    # True
print(is_valid_id("A-2047"))     # False (faqat 1 harf)
print(is_valid_id("xAB-2047"))   # False (kichik harf + qo'shimcha)

# ============================================================
# TASK 9 — Uch regex funksiyasini solishtirish
# ============================================================
# MAQSAD: search(), match(), fullmatch() farqlarini tushunish.
#
# MANTIQ:
# - search()     -> ISTALGAN joydan qidiradi
# - match()      -> faqat BOSHIDAN qidiradi (oxirigacha shart emas)
# - fullmatch()  -> butun satr mos kelishi SHART

print("\n===== TASK 9 =====")

pattern = r"[0-9]+"
text = "Room 204"

print("search:", bool(re.search(pattern, text)))      # True
# search -> "204" ni topadi (matn ichidan)

print("match:", bool(re.match(pattern, text)))        # False
# match -> boshidan tekshiradi: "Room..." -> "R" raqam emas

print("fullmatch:", bool(re.fullmatch(pattern, text)))  # False
# fullmatch -> butun satr faqat raqamlardan iborat bo'lishi kerak

print("fullmatch('204'):", bool(re.fullmatch(pattern, "204")))  # True
# "204" -> butun satr raqamlardan iborat

# ============================================================
# TASK 10 — Sanalarni topish (nomzodlar)
# ============================================================
# MAQSAD: DD/MM/YYYY shaklidagi qismlarni topish.
#
# MANTIQ:
# - [0-9]{2} -> aniq 2 raqam
# - /        -> qiyshiq chiziq
# - findall  -> barcha mosliklarni topadi
#
# MUHIM: Mos kelish sana MAVJUDLIGINI bildirmaydi!
# "99/99/2026" ham 2/2/4 raqam shakliga mos keladi, lekin bunday
# sana yo'q.

print("\n===== TASK 10 =====")

text = "Due 28/09/2026; revised 02/10/2026; invalid 99/99/2026"
dates = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", text)
print("dates:", dates)
# ['28/09/2026', '02/10/2026', '99/99/2026']

# IZOH: "99/99/2026" ham mos keldi, chunki regex faqat
# RAQAM SHAKLINI tekshiradi, mantiqiy to'g'riligini emas.

# ============================================================
# TASK 11 — Emailga o'xshash tokenlarni topish
# ============================================================
# MAQSAD: Oddiy email patterni.
#
# MANTIQ:
# - [A-Za-z0-9._]+ -> harflar, raqamlar, nuqta, pastki chiziq
# - @             -> @ belgisi
# - [A-Za-z0-9.]+ -> domen qismi

print("\n===== TASK 11 =====")

text = "Contact ada@example.com or bob.smith@nsu.ru"
emails = re.findall(r"[A-Za-z0-9._]+@[A-Za-z0-9.]+", text)
print("emails:", emails)
# ['ada@example.com', 'bob.smith@nsu.ru']

# IZOH: Bu O'QUV patterni, to'liq email validatsiyasi EMAS.
# Haqiqiy email tekshiruvi ancha murakkab (RFC 5322 standarti).

# ============================================================
# TASK 12 — Kodlarni tozalash va tanlash
# ============================================================
# MAQSAD: strip + upper + regex filtrlash.
#
# MANTIQ:
# - Har bir qiymatni strip() va upper() qilamiz
# - Keyin fullmatch bilan tekshiramiz

print("\n===== TASK 12 =====")

values = [" ns-205 ", "AB-2047", "invalid", " xy-3001 "]

cleaned = [v.strip().upper() for v in values]
print("cleaned:", cleaned)
# ['NS-205', 'AB-2047', 'INVALID', 'XY-3001']

pattern = r"[A-Z]{2}-[0-9]{4}"
valid = [v for v in cleaned if re.fullmatch(pattern, v)]
print("valid:", valid)
# ['AB-2047', 'XY-3001']

# ============================================================
# BONUS TASK 13 — Katta harf bilan boshlanuvchi so'zlar
# ============================================================
# MAQSAD: [A-Z] bilan boshlanuvchi so'zlarni topish.
#
# MANTIQ:
# - [A-Z]      -> katta harf
# - [a-z]*     -> keyin kichik harflar (ixtiyoriy)
# - findall    -> barcha mosliklar

print("\n===== BONUS TASK 13 =====")

text = "Alice met Bob in Novosibirsk"
capitalized = re.findall(r"[A-Z][a-z]*", text)
print("capitalized:", capitalized)
# ['Alice', 'Bob', 'Novosibirsk']

# ============================================================
# BONUS TASK 14 — Ikki xil kod formati
# ============================================================
# MAQSAD: ? bilan ixtiyoriy belgi.
#
# MANTIQ:
# - AA-123  yoki AA-1234
# - [0-9]{3}[0-9]? -> 3 yoki 4 raqam
# - ? -> oldingi belgi 0 yoki 1 marta

print("\n===== BONUS TASK 14 =====")

pattern = r"[A-Z]{2}-[0-9]{3}[0-9]?"

def is_valid_code(value):
    return re.fullmatch(pattern, value) is not None

print(is_valid_code("NS-205"))    # True  (3 raqam)
print(is_valid_code("NS-2047"))   # True  (4 raqam)
print(is_valid_code("N-205"))     # False (faqat 1 harf)

# ============================================================
# YAKUNIY XULOSA
# ============================================================
"""
BU LABDA O'RGANILGAN ASOSIY TUSHUNCHALAR:
------------------------------------------

1. SATR METODLARI
   - strip()      -> bosh/oxir bo'shliqlarni olib tashlaydi
   - lower()/upper()/title() -> registrni o'zgartiradi
   - split()      -> bo'laklarga ajratadi
   -
18:35
join()       -> bo'laklarni birlashtiradi
   - count()      -> substring soni
   - find()       -> indeks yoki -1
   - startswith()/endswith() -> boshi/oxiri tekshiruvi

2. SATRLAR IMMUTABLE
   - Metodlar ASL satrni O'ZGARTIRMAYDI
   - Har doim YANGI satr qaytariladi

3. REGEX ASOSLARI
   - r"..."       -> raw string
   - [0-9]        -> raqam
   - [A-Z]        -> katta harf
   - +            -> 1 yoki ko'p
   - *            -> 0 yoki ko'p
   - ?            -> 0 yoki 1
   - {4}          -> aniq 4 marta

4. RE MODULI FUNKSIYALARI
   - re.findall()   -> barcha mosliklar
   - re.search()    -> istalgan joydan
   - re.match()     -> faqat boshidan
   - re.fullmatch() -> butun satr

5. AMALIY MASLAHATLAR
   - fullmatch -> to'liq validatsiya uchun
   - search    -> matn ichidan qidirish uchun
   - findall   -> barcha topilmalar uchun
   - Regex FAQAT shaklni tekshiradi, mantiqni emas
   - To'liq email validatsiyasi uchun maxsus kutubxonalar kerak
"""