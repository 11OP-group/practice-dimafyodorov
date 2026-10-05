# Задача: Провести полный рефакторинг этого кода, т.е. переписать его так, чтобы он стал чистым, читаемым и профессиональным.
import sys
from typing import Final

PRICE_PER_LITER: Final[float] = 49.5


def calc_fuel_required(distance: float, consumption: float) -> float:
    """Вычисляет, сколько топлива понадобился.

    Args:
        distance (float): дистанция в км.
        consumption (float): расход на 100 км.

    Returns:
        float: количество литров топлива, округлённое до двух знаков после запятой.
    """
    return distance * (consumption / 100)


def main() -> None:
    """Точка входа.
    Запрашивает у пользователя данные, рассчитывает стоимость поездки, выводит в консоль и обрабатывает возможные ошибки.

    Raises:
        SystemExit: Если введены некорректные данные или прерван ввод.
    """
    try:
        distance = float(input("Введите расстояние в км> "))
        consumption = float(input("Введите расход в литрах на 100 км> "))
    except ValueError:
        print(
            "\n\033[31mЧисла должны быть действительными!\nПопробуйте ещё раз. \033[0m",
            file=sys.stderr,
        )
        sys.exit(1)

    except KeyboardInterrupt:
        sys.exit("\n\nПока\n")

    fuel = calc_fuel_required(distance, consumption)
    cost = fuel * PRICE_PER_LITER

    print(f"""
Нужно {fuel:.2f} литров бензина
Стоимость - {cost:.2f} руб.
    """)


if __name__ == "__main__":
    main()
