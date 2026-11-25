import math

xs = [int(i) for i in input("Введите числа> ").split()]

pair_count = 0
for i in set(xs):
    pair_count += math.floor(xs.count(i)/2)

print(f"Всего пар числе: {pair_count}")