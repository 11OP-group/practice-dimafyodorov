acc = []

while (num := int(input("Введите число> "))) % 7 == 0:
    acc.append(num)

print(f"Ваша последовательно - {acc}")
