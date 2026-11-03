import sys

try:
    a, b, c = map(
        float,
        input("Введите стороны треугольника (A, B, C)> ").split(),
    )
except ValueError:
    print(
        "\n\033[31mСтороны должны быть действительными числами!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

if a <= 0 or b <= 0 or c <= 0:
    print(
        "\n\033[31mСтороны должны быть больше 0!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
elif not (a + b > c and b + c > a and c + a > b):
    print(
        "\n\033[31mТреугольник с такими сторонами не существует!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )

elif a == b == c:
    print("Треугольник - равносторонний")
# elif len({a, b, c}) == 2:
elif a == b or b == c or a == c:
    print("Треугольник - равнобедренный")
else:
    print("Треугольник - разносторонний")
