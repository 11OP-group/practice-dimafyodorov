PASSWORD = "admin"
attempts = 3

while True:
    if input("Введите пароль> ") == PASSWORD:
        print("Доступ разрешён")
        break

    attempts -= 1

    if attempts == 0:
        print("Вход заблокирован")
        break
