account = 1000

while True:
    print("""
1. Узнать баланс
2. Снять 100 руб
3. Положить 100 руб
4. Выход
""")

    match input("Выберете пункт> ").strip():
        case "1":
            print(f"Ваш баланс - {account}")

        case "2":
            if account >= 100:
                account -= 100
                print("Снято")
            else:
                print("Недостаточно средств")

        case "3":
            account += 100
            print("Пополнено")

        case "4":
            print("До свидания")
            break

        case _:
            print("Неверная команда")
