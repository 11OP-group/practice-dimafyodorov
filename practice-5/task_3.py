import sys


def convert_usd_to_rub(amount_usd):
    """Перевод долларов в рубли.

    Args:
        amount_usd (float): Сумма в долларах.

    Returns:
        float: Сумма в рублях.
    """
    USD_TO_RUB = 95.50

    return amount_usd * USD_TO_RUB


try:
    amount = float(input("Введите сумму (usd)> "))
except ValueError:
    print(
        "\n\033[31mСумма должна быть действительным числом!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


print(f"Ваша сумма в рублях - {convert_usd_to_rub(amount)}")
