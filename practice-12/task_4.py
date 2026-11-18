import random

# Т.к. попросили через random создаю случайный список из 10 элементов
marks = []
for _ in range(10):
    marks.append(random.randint(1, 5))

# Решение
counter_5 = 0
counter_2 = 0

for mark in marks:
    if mark == 5:
        counter_5 += 1
    elif mark == 2:
        counter_2 += 1

# print(marks)
print(f"Двоек: {counter_2}\nПятёрок: {counter_5}")