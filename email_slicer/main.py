# def main():
#     print("----------Welcome to Email slicer---------")
#     print("") 

#     input_email = input("Enter your Email to slice : ")
#     (user_name, domain) = input_email.split("@")
#     (domain, extension) = domain.split(".")

#     print(f"User Name : {user_name}")
#     print(f"Domian : {domain}")
#     print(f"Extension : {extension}") 

# while True:
#     main() 
#     break





# def hello ():
#     print("Hello.World") 
#     variable = "Hello . World"

#     (h,c) =  variable.split(".")
#     (c, d) = variable.split("")

#     print(f"c h is : {h}")  
#     print(f"c is {c}")
#     print(f"d is : {d}")
# hello()    

def slice_gmail ():
    print("Welcome to Email slice")
    print("")
    input_email = input("Enter Your Email to slice: ")

    (name,domain) = input_email.split("@")
    (domain, extesion) = domain.split(".")

    print(f"name : {name}")
    print(f"domain: {domain}")
    print(f"Extension : {extesion}")

while True:
    slice_gmail()    
    