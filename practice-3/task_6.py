# Задание 6: "Анкета студента" из презентации!
import sys

# Ввод
try:
    name = input("Введите имя:\n> ")
    age_str = input("Введите возраст:\n> ")
    subject_str = input("Введите любимые предметы (через запятую):\n> ")
# Выхожу если нажать ctrl+c, а почему нет?)
except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

# Обработка
try:
    age = int(age_str)
except ValueError:
    print(
        # "\n\033[31m" и "\033[0m" для то что бы текст был красным
        "\n\033[31mВозрост должен быть целым числом! \nПопробуйте ещё раз. \033[0m",
        # Это ошибка, так что пишу в стандартный поток вывода ошибок
        file=sys.stderr,
    )
    # Завершаю программу
    sys.exit(1)

# Разделяем строчку по запятым, и из подстрочек создаётся список
subject = subject_str.split(",")

student = {
    "name": name,
    "age": age,
    "subject": subject,
}

# Вывод
print("\n" + "=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

print(f"""
Имя: {student["name"]}
Возраст: {student["age"]}
Любимые предметы: {student["subject"]}
""")

print("=" * 30)
