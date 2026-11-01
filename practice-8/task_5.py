import sys

try:
    n = int(input("Введите n> "))
    xs = []
    for _ in range(n):
        xs.append(int(input("Введите число> ")))

except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)


first_place = second_place = float("-inf")

for x in xs:
    if x > first_place:
        second_place = first_place
        first_place = x

    elif x > second_place:
        second_place = x

print(f"Максимально - {first_place}\nВторое по величине - {second_place}")
