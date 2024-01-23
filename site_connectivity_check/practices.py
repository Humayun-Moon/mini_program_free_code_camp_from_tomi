from urllib import request as r 
name = input("Enter your name : ")
print(f"Hello, {name} welcome to site connectivity check program")
# user = input("Would you like to check your web site connectivity(yes or no): ").lower()


def check_site_connectivity(url):
    print(f"Your {url} has been proccesing")
    response = r.urlopen(url)

    print(f"Your {url} response code is : {response.getcode()}") 
while True:    
    user = input("Would you like to check your web site connectivity(yes or no): ").lower()

    if user != "yes":
        print("Please, try to understand our requirements and try again")
        continue
    else:
        user_url = input("Enter URL: ")   
        check_site_connectivity(user_url)
        break 

    