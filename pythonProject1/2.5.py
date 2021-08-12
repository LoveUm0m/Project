prices = [57.8, 46.51, 97, 19.9, 29.9, 36, 44, 59, 99.9, 150]
prices.sort()
for price in prices:
    r = int(price)
    kk = (price - int(price)) * 100
    print(f'{r} руб {kk:02.0f} коп')

print('Топ 5 дорогих товаров:')
for price in sorted(prices)[::-1][:5]:
    r = int(price)
    kk = (price - int(price)) * 100
    print(f'{r} руб {kk:02.0f} коп')