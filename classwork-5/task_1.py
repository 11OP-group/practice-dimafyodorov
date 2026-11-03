counter = 0

while input("Введите слово> ").lower() not in ["стоп", "хватит", "достаточно"]:
    counter += 1

print(counter)
