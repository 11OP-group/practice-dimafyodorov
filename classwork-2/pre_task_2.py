month_number = input("Введите номер месяца> ")

match month_number:
    case "12" | "1" | "2":
        season = "Зима"
        season_emoji = "❄️"
    case "3" | "4" | "5":
        season = "Весна"
        season_emoji = "🌱"
    case "6" | "7" | "8":
        season = "Лето"
        season_emoji = "☀️"
    case "9" | "10" | "11":
        season = "Осень"
        season_emoji = "🍁"
    case _:
        season = "Неизвестно"
        season_emoji = "❌"

print(f"{month_number} | {season} | {season_emoji}")
