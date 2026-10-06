import sys

try:
    weight = int(input("Введите вес> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


if not (0 < weight < 69):
    print(
        "\n\033[31mВес должен быть от 0 до 69 (невключительно)!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
elif weight < 60:
    print("Лёгкий вес")
elif weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")
