#1
favour_word='картошка'
print(favour_word)


#2
first_name = "Виталий"
last_name = "Красилов"

new_account = last_name[:5]
temp_password = last_name[2:6]

print("first name", first_name)
print("last name", last_name)
print("new account", new_account)
print("temporary password", temp_password)


#3
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

first_name = "Виталий"
last_name = "Красилов"

new_account = account_generator(first_name, last_name)
print("new account", new_account)


#4
def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]

first_name = "Виталий"
last_name = "Красилов"

temp_password = password_generator(first_name, last_name)
print("temporary password", temp_password)


#5
company_motto = "Мечты сбываются"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

print("second to last character", second_to_last)
print("last 4 characters", final_word)


#6
first_name = "Боб"
fixed_first_name = "Р" + first_name[1:]

print("исправленное имя", fixed_first_name)


#7
password = "theycallme\"crazy\"91"
print(password)


#8
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print("original title", poem_title)
print("fixed title", poem_title_fixed)




