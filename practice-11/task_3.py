# Считаем степени заранее
# power_by_5 = [i**5 for i in range(151)]
power_by_5 = []
for i in range(151):
    power_by_5.append(i**5)

# e<=150 Так что 150^5 максимально число
max_value = power_by_5[150]

for a in range(1, 151):
    sum_a = power_by_5[a]
    # Т.к. сложение коммутативно, предположим что a <= b <= c <= d и избежим дублирующих комбинаций
    for b in range(a, 151):
        # a^5 + b^5
        sum_ab = sum_a + power_by_5[b]
        # Сумма не может превышать e
        if sum_ab >= max_value:
            break
        for c in range(b, 151):
            sum_abc = sum_ab + power_by_5[c]
            if sum_abc >= max_value:
                break
            for d in range(c, 151):
                sum_abcd = sum_abc + power_by_5[d]
                if sum_abcd > max_value:
                    break

                if sum_abcd in power_by_5:
                    e = power_by_5.index(sum_abcd)
                    # print(f"{a=}, {b=}, {c=}, {d=}, {e=}")
                    # print(f"a+b+c+d={a + b + c + d + e}")
                    # print(f"e^5={sum_abcd}")

                    print(a + b + c + d + e)

                    # Строго говоря не сказано, что лишь 1 решение до 150, но что бы не ждать, т.к. ответ известен
                    exit()

# Ответ: 498
# Примерное время: 22,49s user 0,08s system 98% cpu 22,982 total

# Наверняка можно лучше
# Возможно как-то ограничить верхнюю границу циклов
# + Последняя проверка проходит по всему листу (дважды), что медленно
# Как вариант взять бинарный поиск т.к. power_by_5 только возрастает
