START = 1
STOP = 20

print(f"Нечётные числа от {START} до {STOP}")

print("\nЧерез шаг range()")

for i in range(START, STOP, 2):
    print(i)

print("\nЧерез continue")

for i in range(START, STOP + 1):
    if i % 2 == 0:
        continue

    print(i)

# В плане через continue при НЕ выполнении условия?
print("\nЧерез else")

for i in range(START, STOP + 1):
    if i % 2 != 0:
        print(i)
    else:
        continue
