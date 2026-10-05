import sys

TAX_RATE = 0.13


def pretty_format_rub(amount):
    """Форматирует число в строку как сумму в рублях.

    Args:
        amount (float): Число, которое нужно форматировать.

    Examples:
        >>> pretty_format_rub(123456.789)
        '123 456.79 руб.'

    Returns:
        str: Строка содержащая число, округлённое до сотых, использующая в качестве разделителя пробелы и с припиской "руб." в конце.
    """

    return f"{amount:_.2f} руб.".replace("_", " ")


try:
    income = float(input("Введите годовой доход> "))
except ValueError:
    print(
        "\n\033[31mДоход должен быть действительным числом!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


tax = income * TAX_RATE
net_income = income - tax

print(f"""
        Общая сумма дохода - {pretty_format_rub(income)}
Сумма рассчитанного налога - {pretty_format_rub(tax)}
 Сумма после вычета налога - {pretty_format_rub(net_income)}
""")
