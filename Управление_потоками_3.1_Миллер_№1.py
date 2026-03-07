import random
name = "кирилл"
question = "завтра снег?"
answer = ""

random_number = random.randint(1,9)

if random_number == 1:
    answer = "да, безусловно."
elif random_number == 2:
    answer = "это решительно так."
elif random_number == 3:
    answer = "без сомнения."
elif random_number == 4:
    answer = "ответ туманный, попробуйте еще раз."
elif random_number == 5:
    answer = "спросите еще раз позже."
elif random_number == 6:
    answer = "лучше не говорить вам сейчас."
elif random_number == 7:
    answer = "мои источники говорят «нет»."
elif random_number == 8:
    answer = "прогноз не очень хороший."
elif random_number == 9:
    answer = "очень сомнительно."
else:
    answer = "ошибка"

if question == "":
    print("Вы не задали вопрос. Магический шар не может дать ответ.")
else:
    if name == "":
        print(f"вопрос: {question}")
    else:
        print(f"{name} спрашивает: {question}")
    print(f"магический шар отвечает: {answer}")
