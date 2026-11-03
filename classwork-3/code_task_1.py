import sys

try:
    a = int(input("Введите первое число> "))
    b = int(input("Введите второе число> "))
except ValueError:
    print(
        "\n\033[31mОба числа должны быть целыми!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)


if b % 2 == 0:
    sum_before_b = b // 2
else:
    sum_before_b = -(b + 1) // 2

# Т.к. от А включительно, то исключаем его из того что будет вычитать
temp = a - 1

if temp % 2 == 0:
    sum_before_a = temp // 2
else:
    sum_before_a = -(temp + 1) // 2

result = sum_before_b - sum_before_a

print(result)
