import string
import random 

characters = list(string.ascii_letters + string.digits+ " !@#$%^&()")

def generate_password ():

    password_length = int(input("How long would you like your password to be?: "))

    random.shuffle(characters) 

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)

    password = "".join(password)
    print(password) 
        

while True:
    option = input("Would you like to generate a password? (Yes/No): ").lower()
    if option == "yes":
        generate_password()
    elif option =="no":
        print("Program finised try again with another way")
        continue
    else:
        print("Invalid input, please input yes or no")
        




