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

# Что бы условие m<=n всегда выполнялось, даже при неправильном вводе
if m > n:
    m, n = n, m

for i in range(m, n + 1):
    if (
        (i % 17 == 0)
        or (i % 10 == 9)
        # Кратно 3 И 5 одновременно, т.к. 3*5=15
        or (i % 15 == 0)
    ):
        continue

    print(i)
