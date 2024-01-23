from cricket import cricket as c
from football import football as f

print("Wecome for come to play.")
user_name = input("What's your name : ")
user_age = int(input("Your age: "))
user_email = input("Enter your Email: ")
# user_balance = float(input("How much money you want to play: ")) 

def get_slice_email():
    (user,domain) = user_email.split("@")
    (domain,extension) =domain.split(".") 
    print(f"User Name : {user}")
    print(f"Domain    : {domain}")
    print(f"Extension : {extension}")
get_slice_email()

game_options = ["1. Football" " 2. Cricket"] 

for game in game_options:
    print(game, end=" ")
print() 
user_choice = int(input("What game you want play: ")) 

if user_choice == 1:
      f()
elif user_choice == 2:
      c()      
else:
      print("Something else")
      print("Try again") 


     