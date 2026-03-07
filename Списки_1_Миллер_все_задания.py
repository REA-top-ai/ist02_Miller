#1
cake=['торт',1]
print(cake)


#2
household_chemicals=[['стиральный порошок',1],['средство для мытья посуды',1],['торт',1]]
print(household_chemicals)


#3
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(Names, dogs_names)
print(list(names_and_dogs_names))


#4
orders = ['маргаритки', 'васильки']
print("Сегодняшние заказы:", orders)

orders.append('тюльпаны')
orders.append('розы')

print("обновленные заказы", orders)


#5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

new_orders = orders + ['сирень', 'ирис']
print(new_orders)


broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)


#6
list1 = list(range(0, 9))
print(list1)


list2 = list(range(0, 8))
print(list2)


#7
list1 = list(range(5, 15, 3))
print(list1)


list2 = list(range(0, 40, 5))
print(list2)


#8
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)

all_ages = [32, 41, 29] + age
print(all_ages)

name_and_age = zip(first_names, all_ages)
print(list(name_and_age))

ids = range(4)
print(list(ids))


