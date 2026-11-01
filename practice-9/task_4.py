num_str = input("Введите число> ")

l = len(num_str)
i = 0
last_digit = num_str[-1]

ultimate_counter = {
    "3": 0,
    "last_digit": 0,
    "even": 0,
    "sum >5": 0,
    "mult >7": 1,
    "0 or 5": 0,
}

while i < l:
    current_digit = num_str[i]
    current_digit_int = int(current_digit)

    if current_digit == "3":
        ultimate_counter["3"] += 1

    if current_digit == last_digit:
        ultimate_counter["last_digit"] += 1

    if current_digit_int % 2 == 0:
        ultimate_counter["even"] += 1

    if current_digit_int > 5:
        ultimate_counter["sum >5"] += current_digit_int

    if current_digit_int > 7:
        ultimate_counter["mult >7"] *= current_digit_int

    if current_digit in ("0", "5"):
        ultimate_counter["0 or 5"] += 1

    i += 1

print(f"""
количество цифр 3 - {ultimate_counter["3"]}
сколько раз в нём встречается последняя цифра - {ultimate_counter["last_digit"]}
количество чётных цифр - {ultimate_counter["even"]}
сумму его цифр, больших пяти - {ultimate_counter["sum >5"]}
произведение цифр, больших семи - {ultimate_counter["mult >7"]}
сколько раз в нём встречаются цифры 0 и 5 - {ultimate_counter["0 or 5"]}
""")
