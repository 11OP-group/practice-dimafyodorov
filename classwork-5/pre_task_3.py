import random

number = random.randint(1, 100)
counter = 1

while (guess := int(input("Введите число> "))) != number:
    counter += 1

    if guess > number:
        print("Неверно, меньше")
    else:
        print("Неверно, больше")

print(f"Угадали!\nВам потребовалось {counter} попыток")
