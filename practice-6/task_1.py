import sys

SICK_TOP_TEMPERATURE = 38
NORMAL_TOP_TEMPERATURE = 36
SICK_BOTTOM_TEMPERATURE = 35
NORMAL_BOTTOM_TEMPERATURE = 37

SICK_TOP_PRESSURE = 140
NORMAL_TOP_PRESSURE = 130
SICK_BOTTOM_PRESSURE = 105
NORMAL_BOTTOM_PRESSURE = 110

SICK_TOP_PULSE = 110
NORMAL_TOP_PULSE = 100
SICK_BOTTOM_PULSE = 55
NORMAL_BOTTOM_PULSE = 60


try:
    temperature = float(input("Введите тепреатуру (°C)> "))
    pressure = float(input("Введите давление (верхнее)> "))
    pulse = float(input("Введите пульс (уд/мин)> "))
except ValueError:
    print(
        "\n\033[31mВаши параметры должны быть действительными числами!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

# Проверяем что хотя бы 1 сильно отходит от нормы
if (
    not (SICK_BOTTOM_TEMPERATURE <= temperature <= SICK_TOP_TEMPERATURE)
    or not (SICK_BOTTOM_PRESSURE <= pressure <= SICK_TOP_PRESSURE)
    or not (SICK_BOTTOM_PULSE <= pulse <= SICK_TOP_PULSE)
):
    print("Требуется врач")

# Что всё в пределах нормы
elif (
    (NORMAL_BOTTOM_TEMPERATURE < temperature < NORMAL_TOP_TEMPERATURE)
    and (NORMAL_BOTTOM_PRESSURE < pressure < NORMAL_TOP_PRESSURE)
    and (NORMAL_BOTTOM_PULSE < pulse < NORMAL_TOP_PULSE)
):
    print("Нормальное состояние")

# Что все отходят от нормы
# Строго говоря в "Лёгком недомогании", в отличии от "Требуется врач", не сказано "1 и более параметров значительно отклоняются"
# или что-то похожее, так что использую and (хотя логически не уверен что это правильно)
elif (
    not (NORMAL_BOTTOM_TEMPERATURE < temperature < NORMAL_TOP_TEMPERATURE)
    and not (NORMAL_BOTTOM_PRESSURE < pressure < NORMAL_TOP_PRESSURE)
    and not (NORMAL_BOTTOM_PULSE < pulse < NORMAL_TOP_PULSE)
):
    print("Лёгкое недомогание")

# Так как условия выше не покрывают все случае, добавляю else
else:
    print("Неизвестное состояние (или лёгкое недомогание)")

# Я уверен что это можно решить более красиво, но над этим надо подумать...
# Возможно вынести проверки в функцию и изменить структуру констант + надо определиться с "Лёгким недомоганием"
