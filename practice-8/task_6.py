import random
import sys

number = random.randint(1, 10)
print(number)

try:
    for _ in range(3):
        guess = int(input("Введите n> "))

        if guess != number:
            if guess > number:
                print("Неверно, меньше")
            else:
                print("Неверно, больше")

            continue
        else:
            print("Угадали!")
            break
    else:
        print(f"Попытки кончились, загаданное число было - {number}")


except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)
