import string
import random

characters = list(string.ascii_letters + string.digits + " £$%^&*()") 

random.shuffle(characters)

 

while True:
    passwords = []
    user = input("Do you generate your password: (yes/no)> ").lower()
    if user != "yes":
        break
    else:
        password_length = int(input("How long password you want to : ")) 

        for i in range(password_length):
            passwords.append(random.choice(characters))
        random.shuffle(passwords)
        password= "".join(passwords) 
        

        print(f"Your length {password_length} is to : {password}")   

