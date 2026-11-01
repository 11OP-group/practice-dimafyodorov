import sys

try:
    n = int(input("Введите натуральное число> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

i = 1
while i <= n:
    if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
        i += 1
        continue

    print(i)
    i += 1
