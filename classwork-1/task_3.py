import sys

try:
    month = int(input("Введите номер месяца> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


if not (1 <= month <= 12):
    print(
        "\n\033[31mМесяцы бывают от 1 до 12!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )

# Для читаемости имело бы смысл создать словарь или enum, которые заменяют числа на названия месяцев
elif month == 2:
    print("28 или 29 дней")
# elif month == 4 or month == 6 or month == 9 or month == 11:
elif month in {4, 6, 9, 11}:
    print("31 день")
else:
    print("30 дней")
