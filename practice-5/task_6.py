import math
import sys


def calculate_distance(x1, y1, x2, y2):
    """Вычисляет длину отрезка по координатам двух точек.

    Args:
        x1 (float): координата `x` первой точки.
        y1 (float): координата `y` первой точки.
        x2 (float): координата `x` второй точки.
        y2 (float): координата `y` второй точки.

    Returns:
        float: Длина отрезка.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_triangle_area(a, b, c):
    """Вычисление площади треугольника.

    Args:
        a (float): Длина стороны A.
        b (float): Длина стороны B.
        c (float): Длина стороны C.

    Returns:
        float: Площадь треугольника.
    """
    # Не из любых 3 отрезков можно составить треугольник, так что имело бы смысл бросать исключение при невыполнение условия, но if-ов пока нет)
    p = (a + b + c) / 2

    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def input_dot():
    """Получение точки от пользователя.

    Raises:
        SystemExit: Если введены некорректные данные или прерван ввод.

    Returns:
        tuple[float, float]: координаты точки, в формате (x, y).
    """
    try:
        x, y = map(
            float,
            input("Введите координаты (x y)> ").split(),
        )

    except ValueError:
        print("\nКоординаты должны быть действительными числами!\nПопробуйте ещё раз.")
        sys.exit(1)

    except KeyboardInterrupt:
        sys.exit("\n\nПока\n")

    return (x, y)


print("Первая точка:")
x1, y1 = input_dot()
print("Вторая точка:")
x2, y2 = input_dot()
print("Третья точка:")
x3, y3 = input_dot()

triangle_area = calculate_triangle_area(
    calculate_distance(x1, y1, x2, y2),
    calculate_distance(x2, y2, x3, y3),
    calculate_distance(x3, y3, x1, y1),
)

print(f"Площадь треугольника - {triangle_area:.2f}")
