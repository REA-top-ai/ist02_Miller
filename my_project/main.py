from auth import register_user, login_user
from europeana import get_europeana_data, build_prompt, generate_image, save_image

def main():

    print("1 - Register")
    print("2 - Login")

    choice = input("Choose: ")

    username = input("Username: ")
    password = input("Password: ")

    user = None

    if choice == "1":
        user = register_user(username, password)
        print("REGISTERED")

    elif choice == "2":
        user = login_user(username, password)

        if not user:
            print("WRONG LOGIN")
            return

        print("AUTHORIZED")

    else:
        return


    prompt_input = input("Enter prompt: ")

    items = get_europeana_data(user_prompt)
    prompt = build_prompt(user_prompt, items)

    image = generate_image(prompt)

    save_image(image, username)

    print("DONE")

from auth import register_user, login_user
from europeana import (
    get_europeana_data,
    build_prompt,
    generate_image,
    save_image
)

print("1 - Register")
print("2 - Login")

choice = input("Choose: ")

username = input("Username: ")
password = input("Password: ")

user = None

if choice == "1":
    user = register_user(username, password)

elif choice == "2":
    user = login_user(username, password)

if not user:
    print("Access denied")
    exit()

print("AUTHORIZED")

user_prompt = input("Enter your prompt: ")

items = get_europeana_data(user_prompt)

prompt = build_prompt(user_prompt, items)

image = generate_image(prompt)

save_image(image, username)

print("DONE")