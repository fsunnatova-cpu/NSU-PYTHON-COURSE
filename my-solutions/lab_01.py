print("Task 1 — Personal Information")

name = input("Enter your name: ")

age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")
print()

print("Task 2 — Rectangle")  
# 2прямоуголник

width = float(input("Enter width: "))

height = float(input("Enter height: "))

area = width * height

perimeter = 2 * (width + height)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print()


print("Task 3 — Temperature Converter")

celsius = float(input("Enter celsius temperatura: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius}C = {fahrenheit}F")

print()


print("Task 4 — Purchase Calculator")

quantity = int(input("Enter quantity: "))

price = float(input("Enter price for one: "))

total_price = quantity * price

discounted = total_price * 0.10

discounted_price = total_price - discounted

print(f"Total price: {total_price}")
print(f"Discounted price: {discounted_price}")

print()


print("Task 5 — Arithmetic Operators")

a = 17
b = 5

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

print()



print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
taxt_value = "Python"
boolean_value = True

print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(taxt_value))
print(type(boolean_value))


print()



print("Task 7 — Comparisons and Boolean Logic")


age = 22
is_master_student = True


print( age >=23)
print( age < 28)
print( age == 22)
print( age != 27)
print( age >= 18 and is_master_student)
print( age < 18 or is_master_student)
print( not is_master_student)


print()
print( 10, 12, 27)

 
print("programing_languages: ", type("programing_languages"))
print("12:" )
print("Nurota" )
print("Novosibr")

print("/programming_languages:", type("programing_languages"))
print("12:", type("12"))
print("Nurota", type("Nurota"))
print("Novosibr", type("Novosibr"))

print()

print("Taskn- Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers [0])
print(numbers [-1])
print(numbers [1:4])
print(numbers [::2])

word = "Python"
print(word[0])
print(word[-1])
print(word[:3])

print()

print ("Task 10 - Dictionaries and Membershi")

student = {

    "name": "Anna" ,
    "age": 22,
    "city": "Novosibirsk",

}
print(student["name"])
print(student["age"])
print("age" in student)
print("email" in student)

print()

print("Task 11 - Formatted Output")
radius = float(input("Enter the radius of the circle"))
area = 3.14159 * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area}")
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")

print()


print("Task 12 - Trip Cost Calkulator")

distance = float(input("Enter distance in kilometrs: "))
fuel_consuption = float(input("Enter fuel consumption (liters per 100 km): "))
fuel_price = float(input("Enter fuel price per liter: "))


print(f"Required fuel: {"required_liters":.2f}, liters")
print(f"Total trip cost: {"total_cost":.2f}")

print()















