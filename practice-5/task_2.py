import sys

try:
    weight, height = map(
        float,
        input("Введите свой вес (в кг) и рост (в метрах) через пробел> ").split(),
    )
except ValueError:
    print(
        "\n\033[31mВаши параметры должны быть действительными числами!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

# Сюда бы вставить проверку, что вес и рост больше 0, но ладно

bmi = weight / (height**2)

print(f"Ваш ИМТ - {bmi:.1f}")

# Сложно без ветвления, сюда бы ещё определение "категории", по-хорошему)
