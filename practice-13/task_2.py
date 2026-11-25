n = int(input("Введите колличество строк> "))

chars = []
for _ in range(n):
    chars.extend(input("> "))

print(f"Список введённых символов: {chars}")