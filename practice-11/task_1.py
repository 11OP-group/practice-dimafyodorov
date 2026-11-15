for n in range(1, 13):
    for k in range(1, 13 - n):
        m = 12 - n - k
        if 28 * n + 30 * k + 31 * m == 365:
            print(f"{n=}, {k=}, {m=}")
