print("Task 1- Countdown with while")
number = int(input("Input: "))
while number >= 1:
    print(number)
    number -= 1
    print("Go")


print()

print("Task 2 - Repeat until zero")
count = 0
total_sum = 0
number = int(input("Enter an integer: "))
while number != 0:
    count += 1
    total_sum += number
    number = int(input("Enter an integer: "))
    print(f"Count: {count}")
    print(f"Sum: {total_sum}")

print()


print("Task 3 - Valid input with while True ")
while True:
    number = int(input("Enter an integer from 1 to 10: "))
    if 1 <= number <= 10:
        print("Accepted")
        break
    else:
        print("Invalid value")

print()

print("Task 4 - continue in a while loop")
while number <= 20:
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1

print()


print("Task 5 - Search with loop else")
numbers = [4, 8, 12, 16, 21, 24]
for num in numbers:
    if num % 2 != 0:
        print(f"First odd number: {num}")
        break
    else:
        print("All values are even")


print()

print("Task 6- Multiplication table with nested loops")
for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end=" ")


print()
        

print("Task 7 - Dynamic typing")
value = 42
print(value, type(value))

value = 3.14
print(value, type(value))

value = "Python"
print(value, type(value))

value = [1, 2, 3]
print(value, type(value))


print()

print("Task 8 - Equality, identity, and references")
a = [10, 20]
b = [10, 20]
c = a

print(a == b) 
print(a is b)
print(a == c)
print(a is c)


print(id(a))
print(id(b))
print(id(c))

c.append(30)

print(a)
print(b)
print(c)


print()

print("Task 9 - Function:is_even")
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
print(is_even(0))


print("Task 10 - Function: calculate_discount")
def calculate_discount(price, percent):
    final_price = price - price * percent /100
    return final_price

print(calculate_discount(1000, 15))
print(calculate_discount(250, 20))

print()



