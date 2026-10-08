import sys

VALID_BOARD_SET = set(range(1, 9))

try:
    x1, y1 = map(
        int,
        input("Введите координаты первой клетки через пробел>").split(),
    )
    x2, y2 = map(
        int,
        input("Введите координаты второй клетки через пробел>").split(),
    )
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


if {x1, y1, x2, y2} - VALID_BOARD_SET:
    print(
        "\n\033[31mВыход за пределы доски!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
