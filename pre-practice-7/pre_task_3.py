import sys

print("Доступные операторы: +, -, *, /")
try:
    x, opr, y = input("Введите математическое важение> ").split()
except ValueError:
    print(
        "\n\033[31mНекорректное выражение!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    x = float(x)
    y = float(y)
except ValueError:
    print(
        "\n\033[31mЧисла должны быть действительными!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

match (opr, x, y):
    case ("+", a, b):
        res = a + b
    case ("-", a, b):
        res = a - b
    case ("*", a, b):
        res = a * b
    case ("/", a, 0):
        res = "Ошибка! Деление на 0"
    case ("/", a, b):
        res = a / b
    # По заданию, но мне мой вариант больше нравиться)
    # case ("/", a, b):
    #     if b == 0:
    #         res = "Ошибка! Деление на 0"
    #     else:
    #         res = a / b
    case _:
        res = "Ошибка! Неизвестный оператор"

print(f"Результат: {res}")
