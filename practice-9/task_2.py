target_names = ["Александра", "Левона"]
found_first = 0
counter = 0

while name := input("Введите имя участника> "):
    if name in target_names:
        if found_first:
            break

        found_first = True

    elif found_first:
        counter += 1

print(f"Между Александром и Левотом - {counter} человек")
