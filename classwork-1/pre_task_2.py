import sys

try:
    age = int(input("Введите возраст> "))
    has_id = input("У вас есть документы? (Да/Нет)> ").strip().lower() == "да"
    is_member = input("Вы член клуба? (Да/Нет)> ").strip().lower() == "да"
except ValueError:
    print(
        "\n\033[31mВозраст должен быть целым числом!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

except KeyboardInterrupt:
    sys.exit("\n\nПока\n")

# or работает "лениво", так что при выполнении (is_member and has_id) он сразу вернёт True
if (is_member and has_id) or (has_id and (age >= 25)):
    print("\nДобро пожаловать.")
else:
    print("\nПроход запрешён.")
