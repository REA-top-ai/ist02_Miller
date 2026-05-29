from crud import register_user, login_user
from image_generator import generate_image, save_image

print("1 - Register")
print("2 - Login")

choice = input("Choose: ")

username = input("Username: ")
password = input("Password: ")

# РЕГИСТРАЦИЯ
if choice == "1":

    result = register_user(username, password)

    print(result)

# ЛОГИН
token = login_user(username, password)

if not token:
    print("Wrong username or password")

else:
    print("\nAUTHORIZED")

    prompt = input("\nEnter prompt:\n")

    image = generate_image(token, prompt)

    save_image(image, username)