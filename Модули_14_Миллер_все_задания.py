#1
from datetime import datetime

current_time = datetime.now()

print(current_time)


#2
import random
random_list = []

random_list = [random.randint(1, 100) for _ in range(101)]

randomer_number = random.choice(random_list)

print(random_list)
print(randomer_number)


#3
from datetime import datetime

employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000, "М"],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000, "Ж"],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000, "М"],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000, "Ж"],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000, "М"],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000, "М"],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000, "Ж"],]

def programmer_day_bonus(employee):
    if "программист" in employee[1].lower():
        return employee[3] * 0.03
    return 0

def holiday_bonus(employee, date_str):
    date = datetime.strptime(date_str, "%d.%m")

    if date.day == 8 and date.month == 3 and employee[4] == "Ж":
        return 2000

    if date.day == 23 and date.month == 2 and employee[4] == "М":
        return 2000

    return 0


def salary_indexation(employee):
    hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
    today = datetime.now()
    years_worked = (today - hire_date).days / 365

    if years_worked > 10:
        return employee[3] * 0.07
    else:
        return employee[3] * 0.05


def vacation_list(employees):
    today = datetime.now()
    eligible = []

    for employee in employees:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        months_worked = (today - hire_date).days / 30

        if months_worked > 6:
            eligible.append(employee[0])

    return eligible


print("Премия ко дню программиста:")
for emp in employees:
    bonus = programmer_day_bonus(emp)
    if bonus > 0:
        print(emp[0], "-", bonus)

print("\nСписок на отпуск:")
print(vacation_list(employees))


#4
import random

def digit_sum(number):
    return sum(int(digit) for digit in str(number))


admin_number = random.randint(1, 9)
print(f"Загаданное число администрацией: {admin_number}")

print("Выигрышные номера:")

winners_count = 0


for user_number in range(1, 1001):
    if digit_sum(user_number) % admin_number == 0:
        print(user_number)
        winners_count += 1

        if winners_count == 5:
            break

if winners_count == 0:
    print("Победителей нет.")


#5
import random

attempts = int(input("введите количество бросков"))

for _ in range(attempts):
    result = random.choice(["орел", "решка"])
    print(result)


#6
import random

attempts = int(input("введите количество бросков"))

for _ in range(attempts):
    result = random.randint(1, 6)
    print(result)


#7
import random
import string

length = int(input("введите длину пароля"))

letters = string.ascii_letters

password = ''.join(random.choice(letters) for _ in range(length))

print("сгенерированный пароль", password)
