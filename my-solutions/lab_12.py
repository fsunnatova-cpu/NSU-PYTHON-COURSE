"""
NSU Python — Lab 12
NumPy and Pandas

Задания 1–14 — основные практические задания. Задания 15–16 —
необязательные дополнительные задания.
Выполните не менее 10 основных заданий, включая задания 10–14
и не менее пяти заданий из заданий 1–9. Рекомендуется выполнить все
14 основных заданий.
Используйте только материалы лекции 12 и предыдущих лекций.
Python 3.10 и выше.
Запускайте программу из этой директории. Не изменяйте исходные CSV-файлы.
"""

import numpy as np
import pandas as pd

# ========================================================================
# Task 1 — Create and inspect an array
# ========================================================================
# Создайте np.array([12, 18, 24, 30], dtype=np.int64).
# Выведите массив, shape, ndim, size и dtype.
# Ожидаемые метаданные: (4,), 1, 4, int64.

array = np.array([12, 18, 24, 30], dtype=np.int64)

print("Task 1")
print("Array:", array)
print("Shape:", array.shape)
print("Dimensions:", array.ndim)
print("Size:", array.size)
print("Data type:", array.dtype)


# ========================================================================
# Task 2 — Array creation functions
# ========================================================================
# Создайте массив нулей размером 2 на 3, целочисленный массив из четырёх единиц
# и массив, содержащий 2, 4, 6, 8, с помощью np.arange().
# Используйте np.linspace() для создания пяти равномерно распределённых
# значений от 0 до 1 включительно.
# Ожидаемый результат: [0.0, 0.25, 0.5, 0.75, 1.0].

zeroes = np.zeros((2, 3))
ones = np.ones(4, dtype=int)
sequence = np.arange(2, 10, 2)
values = np.linspace(0, 1, 5)

print("\nTask 2")
print("Array of zeros:\n", zeroes)
print("Array of ones:", ones)
print("Sequence:", sequence)
print("Evenly spaced values:", values)


# ========================================================================
# Task 3 — Indexing and slicing
# ========================================================================
# Для массива a = np.array([10, 20, 30, 40, 50, 60]) выведите:
# первый элемент, последний элемент, элементы с позиции 1 по позицию 3,
# каждый второй элемент, начиная с позиции 0, и массив в обратном порядке.
# Ожидается: 10; 60; [20, 30, 40]; [10, 30, 50];
# [60, 50, 40, 30, 20, 10].

array = np.array([10, 20, 30, 40, 50, 60])

print("\nTask 3")
print("First element:", array[0])
print("Last element:", array[-1])
print("Elements at positions 1 through 3:", array[1:4])
print("Every second element:", array[0::2])
print("Reversed array:", array[::-1])


# ========================================================================
# Task 4 — Reshape and select from a table
# ========================================================================
# Создайте массив np.arange(1, 13).reshape(3, 4).
# Выведите его shape, вторую строку, третий столбец и элемент
# в строке 2, столбце 3.
# Затем выведите транспонированный массив и его shape.
# Индексация начинается с нуля.
# Ожидаемый элемент: 12. Shape транспонированного массива: (4, 3).

table = np.arange(1, 13).reshape(3, 4)

print("\nTask 4")
print("Table:\n", table)
print("Shape:", table.shape)
print("Second row:", table[1])
print("Third column:", table[:, 2])
print("Element at row 2, column 3:", table[2, 3])

transposed = table.T

print("Transposed table:\n", transposed)
print("Transposed shape:", transposed.shape)


# ========================================================================
# Task 5 — Views and independent copies
# ========================================================================
# Создайте a = np.array([10, 20, 30, 40]).
# Создайте view = a[1:3], присвойте view[0] = 99 и выведите a.
# Затем создайте независимую копию independent = a[1:3].copy(),
# присвойте independent[0] = -1 и снова выведите a.
# В обоих случаях результат для a должен быть [10, 99, 30, 40].
# Объясните разницу в комментарии.

a = np.array([10, 20, 30, 40])

view = a[1:3]
view[0] = 99

print("\nTask 5")
print("Array after changing the view:", a)

independent = a[1:3].copy()
independent[0] = -1
print("Array after changing the independent copy:", a)
print("Independent copy:", independent)

# Представление (view) использует ту же область памяти, что и исходный массив.
# Поэтому изменение представления изменяет исходный массив.
# Независимая копия (copy) хранит отдельные данные, поэтому её изменение
# не влияет на исходный массив.


# ========================================================================
# Task 6 — Vectorized calculations and broadcasting
# ========================================================================
# Для a = np.array([2, 4, 6]) вычислите a + 10, a * 3 и a ** 2
# без использования циклов Python.
# Для m = np.array([[1, 2, 3], [4, 5, 6]]) прибавьте
# np.array([10, 20, 30]) к каждой строке с помощью broadcasting.
# Ожидаемая таблица: [[11, 22, 33], [14, 25, 36]].

a = np.array([2, 4, 6])

print("\nTask 6")
print("Original array:", a)
print("a + 10:", a + 10)
print("a * 3:", a * 3)
print("a ** 2:", a ** 2)

m = np.array([[1, 2, 3], [4, 5, 6]])
addition = np.array([10, 20, 30])

broadcast_result = m + addition

print("Original matrix:\n", m)
print("Array to broadcast:", addition)
print("Broadcasting result:\n", broadcast_result)


# ========================================================================
# Task 7 — Boolean filtering
# ========================================================================
# Для scores = np.array([35, 60, 75, 90, 100]) выберите оценки >= 60,
# а затем оценки >= 60 и < 90.
# Используйте булевы маски, оператор & и круглые скобки.
# Не используйте циклы Python.
# Ожидаемые результаты: [60, 75, 90, 100] и [60, 75].

scores = np.array([35, 60, 75, 90, 100])

mask_60 = scores >= 60
mask_60_to_90 = (scores >= 60) & (scores < 90)

print("\nTask 7")
print("Original scores:", scores)
print("Scores >= 60:", scores[mask_60])
print("Scores >= 60 and < 90:", scores[mask_60_to_90])


# ========================================================================
# Task 8 — Aggregations by axis
# ========================================================================
# Для scores = np.array([[70, 80], [90, 85], [50, 60]]) вычислите:
# среднее значение для каждого студента, среднее для каждого задания,
# общее среднее значение, глобальный минимум и максимум.
# Строки представляют студентов.
# Ожидаемые средние по студентам: [75.0, 87.5, 55.0].
# Ожидаемые средние по заданиям: [70.0, 75.0].
# Общее среднее: 72.5. Минимум: 50. Максимум: 90.

scores = np.array([
    [70, 80],
    [90, 85],
    [50, 60]
])

student_means = np.mean(scores, axis=1)
assignment_means = np.mean(scores, axis=0)
overall_mean = np.mean(scores)
minimum = np.min(scores)
maximum = np.max(scores)

print("\nTask 8")
print("Scores:\n", scores)
print("Mean per student:", student_means)
print("Mean per assignment:", assignment_means)
print("Overall mean:", overall_mean)
print("Minimum:", minimum)
print("Maximum:", maximum)


# ========================================================================
# Task 9 — Elementwise and matrix multiplication
# ========================================================================
# Для A = np.array([[1, 2], [3, 4]]) и
# B = np.array([[5, 6], [7, 8]]) вычислите A * B и A @ B.
# Ожидаемый результат поэлементного умножения: [[5, 12], [21, 32]].
# Ожидаемый результат матричного умножения: [[19, 22], [43, 50]].
# Объясните в комментарии, почему результаты отличаются.

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

elementwise_result = A * B
matrix_result = A @ B

print("\nTask 9")
print("A:\n", A)
print("B:\n", B)
print("Elementwise multiplication:\n", elementwise_result)
print("Matrix multiplication:\n", matrix_result)

# При поэлементном умножении перемножаются элементы с одинаковыми индексами.
# При матричном умножении вычисляются скалярные произведения строк и столбцов.
# Поэтому результаты этих операций различаются.
# ========================================================================
# Task 10 — Load and inspect a CSV
# ========================================================================
# Загрузите students.csv с помощью pd.read_csv() в переменную df.
# Выведите head(), shape, названия столбцов, dtypes, info() и describe().
# Ожидаемый shape: (8, 4).
# Ожидаемые столбцы: student_id, name, group, score.
# Вызовите info() напрямую, а не через print(df.info()).
# Не изменяйте CSV-файл.

df = pd.read_csv("students.csv")

print("\nTask 10")
print("First five rows:")
print(df.head())

print("Shape:", df.shape)
print("Column names:", df.columns.tolist())

print("Data types:")
print(df.dtypes)

print("DataFrame information:")
df.info()

print("Statistical summary:")
print(df.describe())


# ========================================================================
# Task 11 — Select and filter labelled data
# ========================================================================
# Повторно загрузите students.csv, чтобы начать задание с исходных данных.
# Выберите столбцы name и score в виде DataFrame.
# Выберите student_id=103 с помощью именованного индекса и loc.
# Ожидаемое имя: Lena.
# Используйте iloc для выбора первых трёх строк.
# Преобразуйте отдельную Series с оценками с помощью
# pd.to_numeric(errors="coerce") для числовых сравнений.
# В исходных данных есть текст "absent".
# Выберите имена студентов с оценками >= 80 и <= 100.
# Ожидаемые имена: Omar, Lena, Sara. Некорректные оценки не должны проходить фильтр.

df = pd.read_csv("students.csv")

print("\nTask 11")
print("Name and score columns:")
print(df[["name", "score"]])

indexed_df = df.set_index("student_id")

print("Student with student_id=103:")
print(indexed_df.loc[103])

print("First three rows using iloc:")
print(df.iloc[:3])

numeric_scores = pd.to_numeric(df["score"], errors="coerce")

valid_high_scores = (
    numeric_scores.ge(80) &
    numeric_scores.le(100)
)

print("Names with scores >= 80 and <= 100:")
print(df.loc[valid_high_scores, "name"])


# ========================================================================
# Task 12 — Clean scores and identify invalid rows
# ========================================================================
# Повторно загрузите students.csv.
# Преобразуйте score с помощью pd.to_numeric(errors="coerce").
# Выведите количество пропущенных или нечисловых оценок после преобразования.
# Ожидаемое значение: 2.
# Считайте некорректными все пропущенные оценки и оценки вне диапазона [0, 100].
# Ожидаемые некорректные student_id: 104, 106, 108.
# Создайте clean = df.loc[valid_mask].copy().
# Ожидаемое количество строк: 5.
# Не заменяйте пропущенные оценки нулём. Объясните почему в комментарии.

df = pd.read_csv("students.csv")

df["score"] = pd.to_numeric(df["score"], errors="coerce")

missing_count = df["score"].isna().sum()

print("\nTask 12")
print("Number of missing or non-numeric scores:", missing_count)

valid_mask = (
    df["score"].notna() &
    df["score"].between(0, 100)
)

invalid_rows = df.loc[~valid_mask]

print("Invalid student IDs:")
print(invalid_rows["student_id"].tolist())

clean = df.loc[valid_mask].copy()

print("Number of valid rows:", len(clean))
print("Cleaned DataFrame:")
print(clean)

# Не заменяем пропущенные оценки нулями, поскольку ноль является допустимым
# числовым значением и исказил бы средний балл.
# Пропущенные и некорректные оценки исключаются из анализа.


# ========================================================================
# Task 13 — Create columns and summarize groups
# ========================================================================
# Используйте clean из задания 12.
# Добавьте passed = score >= 60 и score_fraction = score / 100.
# Отсортируйте данные по score в порядке убывания.
# Выведите общее среднее, процент сдавших и средние значения по группам.
# Ожидаемое общее среднее: 76.0.
# Процент сдавших: 80.0.
# Ожидаемые средние по группам: A=77.5, B=90.0, C=67.5.
# Ожидаемый порядок имён: Lena, Omar, Sara, Anna, Denis.
# Используйте groupby() для расчёта средних по группам.
# Не используйте циклы Python для обработки отдельных строк.

clean["passed"] = clean["score"] >= 60
clean["score_fraction"] = clean["score"] / 100

sorted_clean = clean.sort_values(
    by="score",
    ascending=False
)

overall_mean = clean["score"].mean()
pass_percentage = clean["passed"].mean() * 100
group_means = clean.groupby("group")["score"].mean()

print("\nTask 13")
print("DataFrame with new columns:")
print(clean)

print("Sorted by score descending:")
print(sorted_clean)

print("Overall mean:", overall_mean)
print("Pass percentage:", pass_percentage)
print("Group means:")
print(group_means)


# ========================================================================
# Task 14 — Export an analysis report
# ========================================================================
# Используя clean из заданий 12–13, сохраните cleaned_students.csv
# с параметром index=False.
# Создайте отчёт по группам со столбцами group и mean_score.
# Сохраните его в group_report.csv с index=False,
# затем загрузите файл повторно и проверьте названия столбцов.
# Преобразуйте clean[["score"]] в массив NumPy с dtype=float.
# Ожидаемая форма массива: (5, 1).
# Вычислите среднее значение с помощью NumPy: 76.0.
# Сохраняйте все выходные файлы отдельно от исходного students.csv.

clean.to_csv("cleaned_students.csv", index=False)

group_report = (
    clean.groupby("group", as_index=False)["score"]
    .mean()
    .rename(columns={"score": "mean_score"})
)

group_report.to_csv("group_report.csv", index=False)

reloaded_report = pd.read_csv("group_report.csv")

scores_array = clean[["score"]].to_numpy(dtype=float)

print("\nTask 14")
print("Cleaned data saved to cleaned_students.csv")
print("Cleaned students:")
print(pd.read_csv("cleaned_students.csv"))

print("Group report saved to group_report.csv")
print("Reloaded group report:")
print(reloaded_report)
print("Group report columns:", reloaded_report.columns.tolist())

print("NumPy array:")
print(scores_array)
print("NumPy array shape:", scores_array.shape)
print("NumPy mean:", np.mean(scores_array))


# ========================================================================
# Task 15 — BONUS: weighted assignment scores
# ========================================================================
# Загрузите assignments.csv.
# Преобразуйте test_1 и test_2 в массив NumPy.
# Вычислите итоговые оценки с весами [0.4, 0.6],
# используя матричное умножение.
# Добавьте результаты в DataFrame как столбец final_score.
# Ожидаемые итоговые оценки в порядке строк файла:
# [76.0, 87.0, 56.0, 84.0].
# Выведите имена студентов с итоговой оценкой не ниже 80: Omar и Sara.

assignments = pd.read_csv("assignments.csv")

test_scores = assignments[["test_1", "test_2"]].to_numpy(dtype=float)
weights = np.array([0.4, 0.6])

final_scores = test_scores @ weights

assignments["final_score"] = final_scores

print("\nTask 15")
print("Assignments:")
print(assignments)

print("Final scores:", final_scores)

high_scoring_students = assignments.loc[
    assignments["final_score"] >= 80,
    "name"
]

print("Names with final scores >= 80:")
print(high_scoring_students.tolist())


# ========================================================================
# Task 16 — BONUS: a reusable CSV-analysis function
# ========================================================================
# Определите функцию analyze_scores(input_path, output_path).
# Обязательные столбцы: student_id, name, group, score.
# Если столбцы отсутствуют, вызовите ValueError.
# Преобразуйте и проверьте оценки так же, как в задании 12.
# Если после очистки не осталось допустимых оценок, вызовите ValueError.
# Сохраните очищенную таблицу в output_path и верните словарь, содержащий
# valid_count, invalid_count, mean_score и pass_percentage.
# Для students.csv ожидаются значения 5, 3, 76.0 и 80.0 соответственно.
# Используйте временной или отдельный выходной файл.
# Не перезаписывайте исходный файл.

def analyze_scores(input_path, output_path):
    required_columns = {"student_id", "name", "group", "score"}

    # Проверяем, что входной и выходной файлы имеют разные пути.
    if input_path == output_path:
        raise ValueError("Input and output paths must be different.")

    data = pd.read_csv(input_path)

    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    data["score"] = pd.to_numeric(
        data["score"],
        errors="coerce"
    )

    valid_mask = (
        data["score"].notna() &
        data["score"].between(0, 100)
    )

    valid_data = data.loc[valid_mask].copy()
    invalid_count = int((~valid_mask).sum())

    if valid_data.empty:
        raise ValueError("No valid scores remain after cleaning.")

    valid_data["passed"] = valid_data["score"] >= 60

    mean_score = float(valid_data["score"].mean())
    pass_percentage = float(valid_data["passed"].mean() * 100)

    valid_data.to_csv(output_path, index=False)

    result = {
        "valid_count": len(valid_data),
        "invalid_count": invalid_count,
        "mean_score": mean_score,
        "pass_percentage": pass_percentage
    }

    return result


print("\nTask 16")

analysis_result = analyze_scores(
    "students.csv",
    "students_analysis_cleaned.csv"
)

print("Analysis result:")
print(analysis_result)

print("Valid count:", analysis_result["valid_count"])
print("Invalid count:", analysis_result["invalid_count"])
print("Mean score:", analysis_result["mean_score"])
print("Pass percentage:", analysis_result["pass_percentage"])