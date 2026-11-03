product = 1
while True:
    num = int(input("Введите число> "))

    if num <= 0:
        break

    product *= num

print(product)
