import random
import sys

print("=== Статус заказа ===")
print("Доступные статусы: pending, processing, shipped, delivered, cancelled")

input_status = input("\nВведите статус заказа> ").strip().lower()

# Придумывал
match input_status:
    case "pending":
        status = "В ожидании ⏳"
        description = "Ваш заказ успешно принят и ожидает подтверждения"
        time = "10-30 минут"
        recommendation = "Пожалуйста, проверьте правильность введенных данных"
    case "processing":
        status = "В обработке ⚙️"
        description = "Мы уже собираем и упаковываем товары на складе"

        # Что бы был какой-то случайный диапазон
        rand_base = random.randint(1, 10)
        rand_delta = random.randint(1, rand_base)

        time = f"{rand_base}-{rand_base + rand_delta} часа"
        recommendation = "Скоро мы передадим посылку в службу доставки"
    case "shipped":
        status = "Отправлено ✈️"
        description = "Ваш заказ находится в пути к вам"

        # Что бы был какой-то случайный диапазон
        rand_base = random.randint(1, 10)
        rand_delta = random.randint(1, rand_base)

        time = f"{rand_base}-{rand_base + rand_delta} дней"
        recommendation = "Следите за уведомлениями о доставке"
    case "delivered":
        status = "Доставлено 🟢"
        description = "Посылка успешно прибыла в пункт назначения"
        # До какого числа хранится
        time = f"В пункте выдачи до {random.randint(1, 28)}.{random.randint(1, 12)}"
        recommendation = "Приятного пользования! Будем рады вашему отзыву"
    case "cancelled":
        status = "Отменено ❌"
        description = "Заказ был отменен и не будет выполнен"
        time = "—"
        recommendation = "Если это ошибка, пожалуйста, свяжитесь с поддержкой"
    case _:
        sys.exit(f"""
❌ Ошибка: Неизвестный статус "{input_status}"
Доступные статусы: pending, processing, shipped, delivered, cancelled
""")

print(f"""
╔════════════════════════════════════════╗
║        📦 СТАТУС ВАШЕГО ЗАКАЗА 📦      ║
╚════════════════════════════════════════╝
Статус: {status}
Описание: {description}
Примерное время: {time}
Рекомендация: {recommendation}
""")
