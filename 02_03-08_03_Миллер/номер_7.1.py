days = int(input('введите колво рaбочих дней: '))

salary = 1
s = 0

for days in range(1, days+1):
    s += salary
    salary *= 2

print(f'заработано: {salary/100} за {days} дней')

