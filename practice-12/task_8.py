import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))

min_index = 0
min_number = float("inf")
for i in range(len(numbers)):
    if numbers[i] < min_number:
        min_number = numbers[i]
        min_index = i


print(f"До:    {numbers}")
numbers[0], numbers[min_index] = numbers[min_index], numbers[0]
print(f"После: {numbers}")