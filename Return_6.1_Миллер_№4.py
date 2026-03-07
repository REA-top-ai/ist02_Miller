def check_user_access(user_name, ARM):
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

check_user_access("Дмитрий", 1)
check_user_access("Дмитрий", 2)
check_user_access("Ангелина", 2)
check_user_access("Василий", 1)
