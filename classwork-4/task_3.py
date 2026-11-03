import sys

try:
    m = int(input("Введите первое число> "))
    n = int(input("Введите второе число> "))
except ValueError:
    print(
        "\n\033[31mОба числа должны быть целыми!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
