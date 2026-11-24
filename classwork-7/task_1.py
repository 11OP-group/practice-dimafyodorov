price_str = "100 50 200 150 75 300"

prices = [int(s) for s in price_str.split()]

prices.remove(max(prices))
prices.append(max(prices) * 0.5)
prices.sort()

print(", ".join([str(i) for i in prices]))
print(f"Средняя цена: {max(prices) / len(prices):.2f}")
