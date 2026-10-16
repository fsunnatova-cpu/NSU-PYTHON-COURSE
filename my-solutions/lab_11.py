print("Task 1 Manual iteration")
iterator = iter([10, 20, 30])
print(next(iterator)) #10
print(next(iterator)) #20
print(next(iterator)) #30
print(next(iterator, "END"))

print()

print("Task 2 - Independent iterators")
iter1 = iter(["Anna", "Omar", "Lena"])
iter2 = iter(["Anna", "Omar", "Lena"])

name1_1 = next(iter1) 
name1_2 = next(iter1)

name2_1 = next(iter2)

print(name1_1)
print(name1_2)
print(name2_1)

print(list(iter1))
print(list(iter2))

print()

print("Task 3 - Exhaustion and StopIteration")
iterator3 = iter([2, 4])
while True:
    try:
        value = next(iterator3)
        print(value)
    except StopIteration:
        break

    print()

print("Task 4 - Countdown iterator class")
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

    print()

print("Task 5 - Even-number generator")
def even_numbers(limit):
    for i in range(0, limit,2):
        yield i


print()

print("Task 6 - Square generator")
def squares(numbers):
    for n in numbers:
        yield n * n

print()

print("Task 7 - Generator execution trace")
def trace_values():
    print("Start")
    yield 10
    print("Continue")
    yield 20
    print("End")

gen = trace_values()
print("Created")
print(next(gen))
print(next(gen))
print(next(gen, "DONE"))
print()


print("Task 8 - Generaror expression and reuse")
scores = [45, 60, 75, 90]
passing_scores = (s for s in scores if s >= 60)
print(sum(passing_scores))

print(list(passing_scores))

fresh_passing_scores = (s for s in scores if s >= 60)
count = sum(1 for _ in fresh_passing_scores)
print(count)

print()

print("Task 9 - An infinite sequence with a stopping cobsumer")
def counting(start=1):
    while True:
        yield start 
        start += 1

counter = 0
for value in counting(10):
    print(value)
    counter += 1
    if counter == 5:
        break


print()

print("Task 10 - Read numbers lazily from a file")
def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            if text:
                yield int(text)

print()

print("Task 11 - Logging decorator")

import functools

def announce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@announce
def multiply(a, b=2):
    return a * b

print()

print("Task 12 — Before and after a successful call")
import functools

# Определяем декоратор around, который принимает функцию func
def around(func):
    # functools.wraps сохраняет оригинальное имя и docstring функции
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")  # Печатаем "Before" перед вызовом функции
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию, сохраняем результат
        print("After")   # Печатаем "After" только если вызов прошел успешно
        return result    # Возвращаем сохраненный результат
    
    return wrapper

# Применяем декоратор к функции subtract
@around
def subtract(a, b):
    return a - b

# Проверяем работу
print(subtract(10, 3))


print("Task 13 — Timing a numerical calculation")

import functools
import time

# Определяем декоратор timed
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Засекаем время до начала
        try:
            # Вызываем функцию и сохраняем результат
            result = func(*args, **kwargs)
            return result
        finally:
            # Блок finally выполнится в любом случае (даже если была ошибка)
            end_time = time.perf_counter()  # Засекаем время после
            duration = end_time - start_time
            # Печатаем имя функции и время с 4 знаками после запятой
            print(f"{func.name}: {duration:.4f}s")
    
    return wrapper

# Функция из Task 6 (предполагается, что она уже определена выше в файле)
def squares(iterable):
    for x in iterable:
        yield x * x

# Применяем декоратор к функции sum_squares
@timed
def sum_squares(n):
    # Используем генератор squares и суммируем его
    return sum(squares(range(n)))

# Проверяем работу
print(sum_squares(4))  # Должно вернуть 14

print("Task 14 — Stacked decorators")

# Предполагается, что announce из Task 11 уже определена выше.
# Например:
# def announce(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Running {func.name}")
#         return func(*args, **kwargs)
#     return wrapper

# Применяем декораторы в порядке: сначала @around (Task 12), потом @announce (Task 11)
# Это означает, что announce оборачивает around, а around оборачивает greet.
@announce
@around
def greet(name):
    return f"Hello, {name}"

# Проверяем работу
print(greet("Anna"))

# Объяснение эквивалентного вложенного вызова:
# greet = announce(around(greet))
# То есть при вызове greet("Anna") сначала срабатывает announce, затем around, затем сама greet.