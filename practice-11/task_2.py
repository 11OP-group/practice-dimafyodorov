for i in range((100 // 10) + 1):
    for j in range((100 // 5) + 1):
        for k in range(int(200 // 0.5) + 1):
            if not (i + k + j >= 0):
                continue
            if 10 * i + 5 * j + 0.5 * k == 100:
                print(f"{i:2} быков, {j:2} коров, {k:3} телят")
