fives_count = 0

while 1 <= (grade := int(input("Введите оценку> "))) <= 5:
    if grade == 5:
        fives_count += 1

print(f"У вас - {fives_count} пятёрок")
