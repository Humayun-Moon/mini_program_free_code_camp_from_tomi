import random
import string 

characters = list(string.ascii_letters + string.digits + " *&^%$£?@")

def generate_pass():
    length = int(input("How long would you like your password to be : "))

    random.shuffle(characters)

    passwords = []

    for i in range(length):
        passwords.append(random.choice(characters))
    random.shuffle(passwords) 

    passwords = "".join(passwords)
    return passwords

result = generate_pass()
print(result)


