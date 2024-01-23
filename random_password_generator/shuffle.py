import random 
import string 

characters = list(string.ascii_letters + string.digits + " !@£$%^&")


def new_passwords ():
    password_length = int(input("How long would you like your password to be?:  "))

    random.shuffle(characters)

    passwords = []

    for x in range(password_length):
        passwords.append(random.choice(characters))
    random.shuffle(passwords) 

    passwords = "".join(passwords)  
    print(passwords)

new_passwords()     

