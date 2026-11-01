import sys

try:
    price = int(input("Введите цену> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

counter = {
    25: 0,
    10: 0,
    5: 0,
    1: 0,
}

while price != 0:
    if (price - 25) >= 0:
        price -= 25
        counter[25] += 1

    elif (price - 10) >= 0:
        price -= 10
        counter[10] += 1

    elif (price - 5) >= 0:
        price -= 5
        counter[5] += 1

    else:
        price -= 1
        counter[1] += 1

print(f"""
Вам нужно:
    {counter[25]} монет по 25
    {counter[10]} монет по 10
    {counter[5]} монет по 5
    {counter[1]} монет по 1
""")
