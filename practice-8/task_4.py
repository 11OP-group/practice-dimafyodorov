import math
import sys

try:
    m = int(input("Введите стартовое количество организмов> "))
    p = int(input("Введите среднесуточное увеличение в процентах> "))
    n = int(input("Введите количество дней для размножения> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)


for i in range(1, n + 1):
    print(f"День {i:3}: размер популяции - {m}")
    m = math.ceil(m * (1 + p / 100))
