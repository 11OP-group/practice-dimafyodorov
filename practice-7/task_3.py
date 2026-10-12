import sys

PRICE_COFFEE = 120
PRICE_TEA = 80
PRICE_JUICE = 100
PRICE_WATER = 50
PRICE_LEMONADE = 90

EMOJI_COFFEE = "☕"
EMOJI_TEA = "🍵"
EMOJI_JUICE = "🧃"
EMOJI_WATER = "💧"
EMOJI_LEMONADE = "🥤"

# Возможно слегка избыточно, но мне больше нравится
# + Не уверен как правильно писать docstring к константам (и надо ли)
DISCOUNT = {
    "STUDENT": 0.2,
}
"""dict[str, int]: Проценты скидок для различных промокодов.

Structure:
    Key (str): Название промокода (например, "STUDENT").
    Value (int): Размер скидки в процентах (от 0 до 1).
"""


print("=== Интерактивное меню кафе ===")
print(f"1. Кофе {EMOJI_COFFEE} — {PRICE_COFFEE} руб.")
print(f"2. Чай {EMOJI_TEA} — {PRICE_TEA} руб.")
print(f"3. Сок {EMOJI_JUICE} — {PRICE_JUICE} руб.")
print(f"4. Вода {EMOJI_WATER} — {PRICE_WATER} руб.")
print(f"5. Лимонад {EMOJI_LEMONADE} — {PRICE_LEMONADE} руб.")


# Ввод
user_choice = input("\nВведите номер напитка (1-5) или его название: ").strip().lower()

try:
    quantity = int(input("Введите количество порций: "))

    # Да, raise не проходили, могу int("str") написать
    # Решил попробовать проверку условий здесь сделать
    if quantity <= 0:
        raise ValueError
except ValueError:
    sys.exit(
        "❌ Ошибка ввода: Количество порций должно быть целым положительным числом."
    )

promo_input = (
    input("Введите код скидки (если есть, иначе нажмите Enter): ").strip().upper()
)


match user_choice:
    case "1" | "кофе":
        item_name = "Кофе"
        price = PRICE_COFFEE
        emoji = EMOJI_COFFEE
    case "2" | "чай":
        item_name = "Чай"
        price = PRICE_TEA
        emoji = EMOJI_TEA
    case "3" | "сок":
        item_name = "Сок"
        price = PRICE_JUICE
        emoji = EMOJI_JUICE
    case "4" | "вода":
        item_name = "Вода"
        price = PRICE_WATER
        emoji = EMOJI_WATER
    case "5" | "лимонад":
        item_name = "Лимонад"
        price = PRICE_LEMONADE
        emoji = EMOJI_LEMONADE
    case _:
        sys.exit("❌ Ошибка ввода: Такого напитка нет в меню.")

# Расчёт
initial_sum = price * quantity

discount_amount = 0
if promo_input in DISCOUNT:
    discount_amount = int(initial_sum * DISCOUNT[promo_input])

final_sum = initial_sum - discount_amount


# Вывод
if quantity % 100 in [11, 12, 13, 14]:
    portions_text = "порций"
elif quantity % 10 == 1:
    portions_text = "порция"
elif quantity % 10 in [2, 3, 4]:
    portions_text = "порции"
else:
    portions_text = "порций"


if discount_amount > 0:
    discount_line = (
        f'\nСкидка "{promo_input}" ({DISCOUNT[promo_input]}%): -{discount_amount} руб'
    )
else:
    discount_line = ""


print(f"""
╔════════════════════════════════════════╗
║          {emoji} КВИТАНЦИЯ КАФЕ {emoji}          ║
╚════════════════════════════════════════╝
Товар: {item_name} {emoji}
Цена за порцию: {price} руб
Количество: {quantity} {portions_text}
Сумма: {initial_sum} руб
{discount_line}
══════════════════════════════════════════
 💰 К ОПЛАТЕ: {final_sum} руб
══════════════════════════════════════════""")
