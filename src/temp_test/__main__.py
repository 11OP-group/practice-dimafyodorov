from temp_test import utils


def main():
    initial_amount = float(input("введите сумму> "))
    day = int(input("введите срок (в днях)> "))

    random_rate = utils.random_bank_rate()

    income = utils.bank_model(
        initial_amount,
        day,
        random_rate,
    )
    sum = round(initial_amount + income, 4)

    print(f"Ставка: {random_rate}\nВаш доход: {income}\nИтоговая сумма: {sum}")


if __name__ == "__main__":
    main()
