PIN = "4506"

while True:
    if input("Введите пик-код> ") == PIN:
        print("Доступ разрешён")
        break

    print("Ошибка. Попробуйте еще раз")
