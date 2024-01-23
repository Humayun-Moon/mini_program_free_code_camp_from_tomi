print("Welcome to Email slicer program")

# humayun@gmail.com


user_email = input("Enter you Email to slice: ")

(user,domain) = user_email.split("@")
(domain,extension) = domain.split(".") 

print(f"User name : {user}")
print(f"Domain : {domain}")
print(f"Extension : {extension}")