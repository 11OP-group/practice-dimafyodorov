import sys

try:
    num = int(input("Введите номер> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

if not (0 <= num < 36):
    sys.exit("Ошибка ввода")

elif num == 0:
    color = "Зелёный"

elif (1 <= num <= 10) or (19 <= num <= 36):
    if num % 2 == 0:
        color = "Чёрный"
    else:
        color = "Красный"

else:
    if num % 2 == 0:
        color = "Красный"
    else:
        color = "Чёрный"

print(f"Ваш цвет - {color}")
