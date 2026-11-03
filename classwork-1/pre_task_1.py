import sys

try:
    points = float(input("Введите расстояние в км> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть действительным!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


if not (0 <= points <= 100):
    print(
        "\n\033[31mЧисло должно быть от 0 до 100!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

elif points >= 90:
    print("Оценка 5 (Отлично)")
elif points >= 75:
    print("Оценка 4 (Хорошо)")
elif points >= 60:
    print("Оценка 3 (Удовлетворительно)")
else:
    print("Оценка 2 (Неудовлетворительно)")

print("Результат записан")
