import sys

try:
    amount = int(input("Введите сумму> "))
except ValueError:
    print(
        "\n\033[31mСумма должна быть целым числом!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")


# То что число делиться на 100 и больше 0, надо бы проверять... Но не суть

count_5000 = amount // 5000
amount -= count_5000 * 5000

count_2000 = amount // 2000
amount -= count_2000 * 2000

count_1000 = amount // 1000
amount -= count_1000 * 1000

count_500 = amount // 500
amount -= count_500 * 500

count_200 = amount // 200
amount -= count_200 * 200

count_100 = amount // 100

# Позже понял, что тут наверное лучше использовать словарь и divmod, но уже написано это решение

print(f"""
{count_5000} купюр по 5000 рублей
{count_2000} купюр по 2000 рублей
{count_1000} купюр по 1000 рублей
{count_500} купюр по 500 рублей
{count_200} купюр по 200 рублей
{count_100} купюр по 100 рублей
""")
