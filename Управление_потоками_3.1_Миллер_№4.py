car = input("введите марку машины (Volkswagen Polo / BMW X1): ")
age = int(input("введите ваш возраст: "))
experience = int(input("введите стаж вождения (лет): "))
reputation = int(input("введите коэффициент репутации (1-5): "))
traffic = int(input("введите уровень пробок (1-7): "))
duration = float(input("введите длительность поездки в минутах: "))

tariff = 0

if car == "Volkswagen Polo":
    if 20 <= age <= 27 and 2 <= experience <= 9:
        if 1 <= reputation <= 2 and 1 <= traffic <= 3:
            tariff = 8
        elif 1 <= reputation <= 2 and 4 <= traffic <= 7:
            tariff = 8.5
        elif 3 <= reputation <= 5 and 1 <= traffic <= 3:
            tariff = 7.5
        elif 3 <= reputation <= 5 and 4 <= traffic <= 7:
            tariff = 7.4
    elif 27 <= age <= 34 and 2 <= experience <= 9:
        if 1 <= reputation <= 2 and 1 <= traffic <= 3:
            tariff = 7.2
        elif 3 <= reputation <= 5 and 1 <= traffic <= 3:
            tariff = 7
        elif 3 <= reputation <= 5 and 4 <= traffic <= 7:
            tariff = 7.2
    elif 27 <= age <= 34 and 10 <= experience <= 15:
        if 1 <= reputation <= 2 and 1 <= traffic <= 3:
            tariff = 6.9
        elif 3 <= reputation <= 5 and 4 <= traffic <= 7:
            tariff = 6.6
        elif 1 <= reputation <= 2 and 4 <= traffic <= 7:
            tariff= 6.7


elif car == "BMW X1":
    if 20 <= age <= 27 and 2 <= experience <= 9:
        if 1 <= reputation <= 2 and 1 <= traffic <= 3:
            tariff = 12
        elif 1 <= reputation <= 2 and 4 <= traffic <= 7:
            tariff = 12.5
        elif 3 <= reputation <= 5 and 1 <= traffic <= 3:
            tariff = 11.6
        elif 3 <= reputation <= 5 and 4 <= traffic <= 7:
            tariff = 11.3
    elif 27 <= age <= 34 and 2 <= experience <= 9:
        if 1 <= reputation <= 2 and 1 <= traffic <= 3:
            tariff = 11.4
        elif 3 <= reputation <= 5 and 1 <= traffic <= 3:
            tariff = 11.7
        elif 3 <= reputation <= 5 and 4 <= traffic <= 7:
            tariff = 11.9
    elif 27 <= age <= 34 and 10 <= experience <= 15:
        if 1 <= reputation <= 2 and 1 <= traffic <= 3:
            tariff = 10.8
        elif 3 <= reputation <= 5 and 4 <= traffic <= 7:
            tariff = 10.9
        elif 1 <= reputation <= 2 and 4 <= traffic <= 7:
            tariff = 11


if tariff > 0:
    price = duration * tariff
    print(f"стоимость вашей поездки составит {price}")
else:
    print("для вас тарифа нет")
