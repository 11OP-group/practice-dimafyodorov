import sys

try:
    n = int(input("Введите число> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

counter = 0
for i in range(1, n + 1):
    counter += ((-1) ** (i + 1)) * i

print(counter)
