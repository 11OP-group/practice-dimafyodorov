import random


def random_bank_rate() -> float:
    """
    return rate in [0, 1], round 4 digits
    """
    return round(random.random(), 4)


def bank_model(init: float, time: int, rate: float) -> float:
    one_day = (rate / 365) * init
    income = one_day * time

    return round(income, 4)
