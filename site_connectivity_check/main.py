import urllib.request as r 

def main(url):
    print("Chacking Connectivity")


    response = r.urlopen(url)
    print(f"Connected to {url} successfully ")
    print("The response code was: ", response.getcode())
print(f"This is a site connectivity checker Python program ")
input_url = input("Enter the URL you want to check: ")
main(input_url)