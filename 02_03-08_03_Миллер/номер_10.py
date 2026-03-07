coin_5 = int(input('видете число копеек по 5: '))
coin_10 = int(input('видете число копеек по 10: '))
coin_50 = int(input('видете число копеек по 50: '))

coins = [coin_5 * 5, coin_10 * 10, coin_50 * 50]
s = sum(coins)

if s == 100:
    print('поздравляем')
elif s < 100:
    print(f'сумма {s} меньше 1 рубля')
elif s > 100:
    print(f'сумма {s} больше 1 рубля')


