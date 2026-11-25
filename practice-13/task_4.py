ipv4 = [int(s) for s in input("Введите ip-аддрес> ").split(".")]

if len(ipv4) != 4:
    print("НЕТ")
    print("Должно быть 4 числа разделённых точкой")
    exit()

for i in ipv4:
    flag = i in range(256)
        
if flag:
    print("ДА")
else:
    print("НЕТ")
    print("Числа должны быть в диапозоне от 0 до 255")