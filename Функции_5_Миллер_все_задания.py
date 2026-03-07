# 1
def create_spreadsheet(title):
    print("Создание электронной таблицы с именем " + title)
create_spreadsheet("Загрузки")

def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " с количеством строк " + str(row_count))
create_spreadsheet("Приложения", 10)
