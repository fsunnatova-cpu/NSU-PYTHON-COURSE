
from typing import final


print("Task 1 in Functions")
values = [12, 7, 9, 5, 14]
count = 12
smallest = 7
largest = 9
total = 5
mean = 1.5
print(f"Number of values: {count}")
print(f"Smallest value: {smallest}")
print(f"Total: {largest}")
print(f"Mean: {mean:.2f}")

print()


print("Task 2 - Absolute Value and Rounding")
temperature_change = -7.438
measurement = 19.876554
print(abs(temperature_change))
print(round(measurement, 1))
print(round(measurement, 2))
print(round(measurement, 3))


print()


print("Task 3 - Assignment and Augmented Assignment")
balans = 10000.0
print("balance = balance + 250")
print("balance = balance - 120")
print("balance = balance * 1.05")

print()

print("Task 4 - Operator Precedence")

expression_1 = 2 + 3 * 4
expression_2 = (2 + 3) * 4
expression_3 = 20 / 5 + 3
expression_4 = 20 / (5 + 3)
expression_5 = 2 ** 3 ** 2

print()


print("Task 5 - Time Corversion")
total_seconds = 2
print("minutes = 1")
print("remaing_seconds = 2")

print()


print("Task 6 -Conversion Is Not Always Reversible ")
value = 17.89
integer_value = 17.8
print("float_value = 17.8")

text_value = "17.8"

print()


print("Task 7 -Basic String Operations")
first_name = input("First name:Fotima ")
last_name = input("Last name:Zuxro ")
full_name = "Fotima"

print()


print("Task 8 - Useful print() Options")
language = "Python"
course = "AI and Big Data Analytics"
university = "BXDU"
print()




print("Task 9 — Collections")

student_name = "Fotima"
student_age = 27
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"
print("student = {Fotima}")

print()



print("Task 10 — Mutable and Immutable Objects")
numbers = [11, 22, 30]
same_numbers = numbers


text = "Python"
same_text = text
print()


print("Task 11 - Small Statistics Report")
scores = [78, 93, 85, 69, 88]
print("score_count = 12")
print("minimum_score = 23")
print("maximum_score = 11")
print("mean_score = 12.2")

print()

print("Task 12 — PEP 8 Cleanup")
print("min_score(P=15")
print("max_score(Q=31)")
print("mean_score(D=6)")

print("int(X=P*Q-D/100*P*Q")

print("Final:X",)


print(" Task -12 Optional Challenge — Student Score Summary")

price = 1250
quantity = 3
discount_percent = 10
print()
print("subtotal = price * quantity")
print("discount_amoun = diccount_percent / 100 * subtotal")
print("final_total = subtotal - discount_amount")

print(f"Final: {"final _ total"}" )

print()


print("Optimal Chalenge - Student Score Summary")
print()
student_name = input("Enter student name: ")
score_1 = float(input("Enter first test score: "))
score_2 = float(input("Enter second test score: "))
score_3 = float(input("Enter thirt test score: thirt"))
scores = [score_1, score_2, score_3]

minimum_score = min(scores)
maximum_score = max(scores)
mean_score = sum(scores) / len(scores)

print()
print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Minimum: {minimum_score:.2f}")
print(f"Mean: {mean_score:.2f}")


print()

print("Task 13 - Multiple Assignment")
x, y, z = 10, 20, 30
print(x, y, z)

a = 5
b = 12
a, b = b, a
print()

print("Task 14 - String Methods")

text = " Python Programming Course "
print(text)

print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Course", "Lab"))
cleaned_text = text.strip()
print(cleaned_text.startswith("Python"))
print(cleaned_text.endswith("Course"))

print()


print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))


print()
 
print("Task 16 — Membership")

numbers = [10, 20, 30]
text = "Python Programming"
student = {
    "name": "Anna",
    "age": 22,
    }

print(20 in numbers)
print(50 not in numbers)
print("Python" in text)
print("Java" not in text)
print("age" in student)
print("email" in student)

print()


print("Task 17 — Time Decomposition")


total_seconds = int(input("Enter duration in seconds: "))
print(total_seconds)
hours = total_seconds // 3600
print("hours : " , hours )
remaining_seconds = total_seconds % 3600
print(remaining_seconds)
minutes = remaining_seconds // 60


print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {remaining_seconds} second(s))")
hours = 0
remaining_seconds = 0
minutes = 0
seconds = 0

print()


print("Task 18 — Order Invoice")
price_1 = 0.0
quantity_1 = 0

price_2 = 0.0
quantity_2 = 0

price_3 = 0.0
quantity_3 = 0


price_1 = float(input("Enter price for product 1: "))
quantity_1 = int(input("Enter quantity for product 1: "))

price_2 = float(input("Enter price for product 2: "))
quantity_2 = int(input("Enter quantity for product 2: "))

price_3 = float(input("Enter price for product 3: "))
quantity_3 = int(input("Enter quantity for product 3: "))

product_1_total = 0.0
product_2_total = 0.0
product_3_total = 0.0

subtotal = 0.0
tax = 0.0
final_total = 0.0

product_1_total = price_1 * quantity_1
product_2_total = price_2 * quantity_2
product_3_total = price_3 * quantity_3
       
subtotal = product_1_total + product_2_total + product_3_total
tax = subtotal * 0.05
final_total = subtotal + tax

print(f"Product 1: {product_1_total:.2f}")
print(f"Product 2:{product_2_total:.2f}")
print(f"Product 3:{product_3_total:.2f}")
print("_" * 20)
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {final_total:.2f}")

print()


print("Task 19 — Coordinate Analysis")
x1 = 0.0
y1 = 0.0
x2 = 0.0
y2 = 0.0

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
x3 = float(input("Enter x3: "))
x4 =float(input("Enter x4: " ))
point_1 = ()
point_2 = ()

point_1 = (x1, y1)
point_2 = (x2, y2)

delta_x = 0.0
delta_y = 0.0
distance_squared = 0.0
distance = 0.0

print(f"Point 1: {point_1}")
print(f"Point 2: {point_2}")
print(f"Distance: {distance:.2f}")

      

print()

print("Task 20 — Complex Numbers")
z1 = 3 + 4j
z2 = 2 - 1j

print(z1)
print(z2)
print(type (z1))
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
print(z1 / z2)

print(z1.real)
print(z1.imag)


print()

print("Task 21 — Student Data Record")


student_name = ""
student_age = 0
university = ""

score_1 = 0.0
score_2 = 0.0
score_3 = 0.0

scores = []
student = {}
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
university = input("Enter university name: ")
score_1 = float(input("Enter frist score: "))
score_2 = float(input("Enter second score: "))
score_3 = float(input("Enter third score: "))


student = {
    "name": student_name,
    "age": student_age,
    "university": university,
    "score": scores
}

score_count = 0
minimum_score = 0.0
maximum_score = 0.0
mean_score = 0.0

score_count = len(scores)
minimum_score = min(scores)
maximum_score = max(scores)
mean_score = sum(scores)

print("---Student Report ---")
print(f"Student: {student['name']}")
print(f"Number of scores: {score_count}")
print(f"Minimum score: {minimum_score}")
print(f"Maximum score: {maximum_score}")
print(f"Mean score: {mean_score:.2f}")
print("------------")

print()

print("Task 22 — Debug the Program")
score1 = float(input("Score 1: "))
score2 = float(input("Score 2: "))
score3 = float(input("Score 3: "))
total = score1 + score2 + score3
average = total / 3
print(f"Average: {average}")


print()










 