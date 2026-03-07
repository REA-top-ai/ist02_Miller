maximum = 125
average = 75
minimum = 25
std_deviation = 10

if maximum > average + 5 * std_deviation or minimum < average - 5 * std_deviation:
    print("в ваших данных имеются экстремальные значения и требуют предобработки")
elif maximum > average + 3 * std_deviation or minimum < average - 3 * std_deviation:
    print("в ваших данных имеются выбросы и требуют предобработки")
else:
    print("ваши данные пригодны для анализа")
