import sys

try:
    n = int(input("Введите второе число> "))
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

# Количество чисел от 1 до n, которые делятся на k
div2 = n // 2
div3 = n // 3
div5 = n // 5

div2_3 = n // 6
div2_5 = n // 10
div3_5 = n // 15

div2_3_5 = n // 30

result = n - (div2 + div3 + div5) + (div2_3 + div2_5 + div3_5) - div2_3_5

print(
    f"Количество целых положительных чисел, не превосходящих n, которые не делятся ни на одно из чисел 2,3 и 5 - {result}"
)
