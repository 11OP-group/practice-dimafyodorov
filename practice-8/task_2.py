import sys

try:
    xs = [int(input("Введите число> ")) for _ in range(10)]
except ValueError:
    print(
        "\n\033[31mЧисло должно быть целым!\nПопробуйте ещё раз. \033[0m",
        file=sys.stderr,
    )
    sys.exit(1)

for x in xs:
    if x % 2 != 0:
        print("NO")
        break
else:
    print("YES")

# Или if с all(x % 2 == 0 for x in xs) или типа того
