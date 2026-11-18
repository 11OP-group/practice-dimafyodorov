prices = [1500, 500, 2000, 3500, 1000, 4500]

print(f"Самый дорогой товар:          {max(prices)}")
print(f"Самый дешевый товар:          {min(prices)}")
print(f"Общую стоимость всех товаров: {sum(prices)}")
print(f"Среднюю цену товара:          {(sum(prices)/len(prices))}")