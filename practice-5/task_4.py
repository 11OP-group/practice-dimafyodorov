import math
import sys


def calculate_rectangle_area(width, height):
    """Вычисление площади прямоугольника.

    Args:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.

    Returns:
        float: Площадь прямоугольника.
    """
    return width * heigh


def calculate_circle_area(radius):
    """Вычисление площади круга.

    Args:
        radius (float): Радиус круга.

    Returns:
        float: Площадь круга.
    """
    return math.pi * radius**2


# Возможно не лучшее решение, т.к. try-except захватывает лишнее, но так короче
try:
    width, height = map(
        float,
        input("Введите ширину и высоту прямоугольника через пробел)> ").split(),
    )

    print(f"Площадь прямоугольника - {calculate_rectangle_area(width, height):.2f}\n")

    radius = float(input("Введите радиус круга> "))

    print(f"Площадь круга - {calculate_circle_area(radius):.2f}")

except ValueError:
    print(
        "\n\033[31mЧисла должны быть действительными!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")
