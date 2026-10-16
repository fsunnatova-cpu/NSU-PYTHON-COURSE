print("Task 1 - Positive, negative, or zero")

number = int(input("Enter an integer: "))

if number > 0:
    print(("Positive"))
elif number < 0:
    print("Negativ")
else:
    print("Zero")

    print()
    
    print("Task 2 - Age category")

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 64:
    print("Adult")
else:
    print("Senior")
    #Test boundary valuse: 12, 13, 17, 18, 64, 65.
print()


print("Task 3 - Grade classifier")
# Ask the user for a score.
score = float(input("Enter student score: "))

# First check whether the score is between 0 and 100
if 0 <= score <= 100:
    # For a valid score:
    if score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    else:
        #For an invalid score print:
        print("Invalid score")

        print()    

print("Task 4 - Access decision")
age = int(input("Enter age: "))
ticket = input("Do you have a ticket? (yes/no): ")
#проверяуь условия доступа
if age >= 18 and ticket == "yes":
    print("Ticket required")
else:
    print("Must be 18 or order")    

print()
print("Task 5 - Even numbers with range")
for number in range(2, 31, 2):
        print(number)
        print(*range(2, 31, 2))

        print()

print("Task 6 - Sum of multiples of 3")
total_sum = 0
for number in range(3, 100):
    if number % 3 == 0:
        total_sum += number
print(total_sum) 
print()

print("Task 7 - Count number categories")

numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]
positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif  num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive: ", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)


print()

print("Task 8 - Count vowels")

text = input("Enter a word or short text:")
vowels = "aeiou"
count = 0


for char in text.lower():
    if char in vowels:
        count += 1

print(f"Vowels: {count}")



print()

print("Task 9 - Student results") 
scores = [85, 42, 67, 91, 58, 73, 100, ]
passed = 0
failed = 0
total = 0
for score in scores:
    total += score
    if score >= 60:
        passed += 1
    else:
        failed += 1
average = total / len(scores)

print(f"Passed: {passed}")
print(f"Failed:{failed}")
print(f"Average: {average:.2f}")

print()


print("Task 10 - Search and stop")
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]
target = input("Enter a name: ")
found = False

for name in names:
    print("Found")
    found = True
    break
if not found:
    print("Not found")

    print()


print("Task 11 - Skip invalid scores")
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

valid_scores = []
total = 0
for score in raw_scores:
     if score < 0 or score > 100:
         continue

print(score)     
valid_scores.append(score)
total += score
if len(valid_scores) > 0:
    average = total / len(valid_scores)
else:
    average = 0
print("Valid scores:", valid_scores)
print("Average:", average)
print()


print("Task 12 - Dictionary iteration")
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}
passed_count = 0
for name, score in student_scores.items():
    if score >= 60:
        print(f"{name}: Pass")
        passed_count += 1
    else:
        print(f"Total passed: {passed_count}")
        print()

print("Task 13 - FizzBuzz")  
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 


print()


print("Task 14 - Limited login attempts")
correct_pin = "4821"

for attempt in range(3):
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
    else:
        print("Access denied")

print()


print("Task 15 - Largest of three numbers")
a = int(input("Enter frist number: "))
b = int(input("Enter scond number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Largest: {largest}")


print()

print("Task 16 - Humber statistics")

numbers = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]

positive_count = 0
negative_count = 0
zero_count = 0
positive_count = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
        positive_sum += num
    elif num < 0:
        negative_count += 1
        negative_sum += num
    else:
        zero_count += 1

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")
print(f"Positive sum: {positive_sum}")
print(f"Negative sum: {negative_sum}")

print()


print("Task 17 - Highest and lowest score")
scores = [71, 85, 42, 96, 58, 83, 67, 91]
highets = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print(f"Highers: {highest}")
print(f"Lowest: {lowest}")

print()

print("Task 18 - Temperature analysis")
temperatures = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]
cold_cound = 0
mild_cound = 0
warm_cound = 0
hot_cound = 0

for temp in temperatures:
    if temp < 10:
        category = "Cold"
        cold_count += 1
    elif temp <=19:
        category = "Mild"
        mild_count += 1
    elif temp <= 29:
        category = "Warm"
        warm_count += 1
    else:
        category = "Hot"
        hot_count += 1

    print(f"{temp}: {category}")

print(f"Cold: {cold_count}")
print(f"Mild: {mild_count}")
print(f"Warm: {warm_count}")
print(f"Hot: {hot_count}")     

print()

print("Task 19 - Running balance")
transactions = [500, -120, -80, 250, -700, 300, -200]
balance = 1000

deposits = 0
withdrawals = 0
for transaction in transactions:
    balance += transaction

    if transaction > 0:
        deposits += 1
    else:
        withdrawals += 1

    print(f"Transaction: {transaction}")
    print(f"Balance: {balance}")

print(f"Final balance: {balance}")
print(f"Deposits: {deposits}")
print(f"Withdrawals: {withdrawals}")

print()

print("Task 20 - Find first number divisible by 7 and 11")
for num in range(1, 501):
    if num % 7 == 0 and num % 11 == 0:
        print(num)
        break

print()

print("Task 21 - Limited number guessing")
secret_number = 37


for attemp in range(5):
    guess = int(input("Enter yuor guess: "))

    if guess < "secret_number" :
       print("Too low")
    elif guess > "secret_number" :
        print("Too hugh")
    else:
        print("Correct")
        break
else:
    print("Out of attempts")
    
    
print()

print("Task 22 - Count increases")
values = [10, 14, 13, 18, 22, 20, 25, 25, 30]

increases = 0
for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        increases += 1

print(f"Increases: {increases}")

print()


print("Task 23 - Prime number check")
number = int(input("Enter an integer greate than 1: "))
is_prime = True

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")


print()

print("Task 24 - Multiplication table")
for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end=" ")

print()


print("Task 25 - Second largest value")
numbers = [12, 7, 19, 3, 19, 14, 8]

largest = None
second_largest = None


for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num >second_largest):
        second_largest = num

print(f"Second largest: {second_largest}")



print()

print("Task  26 - Count consecutive positives")
numbers [2, 5, 7, -1, 3, 4, 8, 9, -2, 6]

current_count = 0
longest_count = 0
for num in numbers:
    if num > 0:

        current_count += 1

        if current_count > longest_count:
            londest_count = current_count
        else:
            current_count = 0

print(f"Longest positive sequence: {longest_count}")

print()


print("Task 27 - Number frequency")

numbers = [4, 2, 7, 4, 8, 4, 2, 9, 4, 1]
user_input = int(input("Enter a number: "))
occurrences = 0

for num in numbers:
    if num  == user_input:
        occurrences += 1

print(f"Occurrences: {occurrences}")


print()


print("Task 28 - simple password checker")

password = input("enre password: ")
has_digit = False
has_upper = False


for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Password is valid")
else:
    print("Password is not valid")


print()


print("task 29 - Lokal maximum")
values = [3, 7, 4, 8, 5, 9, 2, 6, 1]

for i in range(1, len(values) - 1):
    if values[i] >values[i - 1] and values[i] > values[i + 1]:
        print(values[i])

print()

print("Task 30 - Pair with target sum")
numbers = [2, 4, 7, 11, 15, 3]
target = 10
found = False
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
            found = True
            break
        if found:
            break

print()

print("Task 31 - Grade distribution")
scores = [95, 82, 67, 73, 58, 91, 49, 88, 76, 100, 61]
count_a = 0
count_b = 0
count_c = 0
count_fail = 0

for score in scores:
    if 90 <= score <= 100:
        count_a += 1
    elif 75 <= score <= 89:
        count_b += 1
    elif 60 <= score <= 74:
        count_c += 1
    else:
        cound_fail += 1

print(f"a: {count_a}")
print(f"B: {count_b}")        
print(f"C: {count_c}")
print(f"Fail: {count_fail}")

max_count = max(count_a, count_b, count_c, count_fail)

if max_count == count_a:
    most_common = "A"
elif max_count == count_b:
    most_common = "B"
elif max_count == count_c:
    most_common = "C"
else:
    most_common = "Fail" 
    print(f"Mast common: {most_common}")


print()


print("Task 32 - Find duplicate values")
numbers = [4, 7, 2, 4, 9, 7, 5, 2]
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            print(numbers[i])
            duplicates.append(numbers[i])

print()

print("Task 33 - Closest number to target")
numbers = [5, 17, 23, 41, 8, 31]
target = 20
closest = numbers[0]
min_diff = abs(numbers[0] - target)
for num in numbers[1:]:
    diff = abs(num - target)
if diff < min_diff:
    min_diff = diff
    closest = num 

print(f"Closest: {closest}")


print()


print("Task 34 - Detect first repeated value")
seen = []

for num in numbers:
    if num in seen:
        print(f"First repeated: {num}")
        break
    else:
        seen.append(num)
print()

print("Task 35 - Prime numbers from 2 to 100")

for num in range(2, 101):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
if is_prime:
    print(num)

print()


print("Task 36 - Number triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")


print()
















    