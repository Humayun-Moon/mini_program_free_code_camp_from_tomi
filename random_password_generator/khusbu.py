import string
import random 

option = input("Do you want to generate passwords(yse or no): ").lower()

if option != "yes":
    print("Try to understand and try again")
    quit()

characters = list(string.ascii_letters + string.digits + "£$%^&*&")

def password_make():
    while True:
        print("Welcome to password generator Python program")
        length = int(input("How long password you want to : "))

        random.shuffle(characters)

        passwords = []

        for i in range(length):
            passwords.append(random.choice(characters))
        random.shuffle(passwords)
        
        get_password = "".join(passwords)
        print(f"Your length {length} password is : {get_password} ")

result = password_make()

# while True:
#     option = input("Do you want to generate passwords(yse or no): ").lower()

#     if option != "yes":
#         break
#     else:
#         print(f"Your expected passwords is : {result}")
#         continue       