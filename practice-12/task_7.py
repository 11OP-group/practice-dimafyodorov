numbers = [10, 20, 30, 40, 50]

target = int(input("Введите число> "))

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"{target} найдено, индектс: {i}")
        break

else:
    print("Нет такого числа")