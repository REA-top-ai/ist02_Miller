#1
print((6 * 6) - 1 == 8 + 1)
print(13 - 7 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)


#2
print((6 * 6) - 1 >= 8 + 1)
print(13 - 7 <= (3 * 2) + 1)
print(3 * (2 - 1) > 4 - 1)


#3
bool_variable = True
print(bool_variable)
print(type(bool_variable))

bool_variable = 'true'
print(bool_variable)
print(type(bool_variable))

bool_variable_2 = False
print(bool_variable_2)
print(type(bool_variable_2))


#4
user_name = "Дмитрий"
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome_message = "Добро пожаловать"

if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome_message)


user_name = "Ангелина"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome_message)


#5
enter_number = 2

if enter_number < 3:
    print(f"Попробуйте еще раз. У вас осталось {3 - enter_number} попыток.")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. "
          "Для разблокировки обратитесь в службу поддержки.")


#6
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

print("statement_one", statement_one)
print("statement_two", statement_two)


#7
user_name = "Дмитрий"
ARM = 1
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"

if (user_name == "Дмитрий" and ARM == 1) or \
   (user_name == "Ангелина" and ARM == 2) or \
   (user_name == "Василий" and ARM == 3) or \
   (user_name == "Екатерина" and ARM == 4):
    print("Добро пожаловать!")
else:
    if user_name == "Дмитрий":
        print(Dmitriy_check)
    else:
        print("Логин или пароль не верный, попробуйте еще раз")

#8
print((2 - 1 > 3) or (-5 * 2 == -10))
print((9 + 5 <= 15) or (7 != 4 + 3))


#9
user_name = "Дмитрий"
ARM = 1
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"

user_ARM_mapping = {
    "Дмитрий": 1,
    "Ангелина": 2,
    "Василий": 3,
    "Екатерина": 4}

if user_name in user_ARM_mapping and ARM == user_ARM_mapping[user_name]:
    print("Добро пожаловать!")
elif user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print("Логин или пароль не верный, попробуйте еще раз")


#10
grade = 4.33

if grade >= 4.0:
    print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0:
    print("C")
elif grade >= 1.0:
    print("D")
elif grade >= 0.0:
    print("F")



