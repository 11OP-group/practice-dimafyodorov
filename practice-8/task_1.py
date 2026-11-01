import sys

try:
    n = int(input("Введите число> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)


print(f"Таблица умноженеия на {n}")

for i in range(1, 11):
    print(f"{i:>2}*{n}={i * n}")
