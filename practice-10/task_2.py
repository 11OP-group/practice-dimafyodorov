n1 = int(input("Введите 1 число> "))

while True:
    n2 = int(input("Введите 2 число> "))

    if n2 <= n1:
        print("Ошибка, число 2 должно быть больше числа 1\n")
    else:
        break

while True:
    n3 = int(input("Введите 3 число> "))

    if n3 <= n2:
        print("Ошибка, число 3 должно быть больше числа 2\n")
    else:
        break

print("Последовательность принята")
