import math
import sys

try:
    grad = float(input("Введите колличество градусов> "))
except ValueError:
    print(
        # "\033[31m" и "\033[0m" для то что бы текст был красным
        "\n\033[31mЧисло должно быть действительным!\nПопробуйте ещё раз. \033[0m",
        # Это ошибка, так что пишу в стандартный поток вывода ошибок
        file=sys.stderr,
    )
    # Завершаю программу
    sys.exit(1)

# Выхожу если нажать ctrl+c, а почему нет?)
except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

rad = math.radians(grad)
formul = math.sin(rad) + math.cos(rad) + (math.tan(rad) ** 2)

# print(f"sin(x)+cos(x)+tg^2(x)={formul}")
print(formul)
