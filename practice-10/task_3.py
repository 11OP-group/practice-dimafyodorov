max_val = float("-inf")

while True:
    x = int(input("Введите число> "))

    if x == 0:
        break
    elif x > max_val:
        max_val = x

print(f"\nМаксимальное число - {max_val}")
