valid_age = False
while not valid_age:
    age = int(input("Введите возраст> "))

    if not (valid_age := 20 < age < 120):
        print("invalid age\n")

print(f"You age - {age}")
