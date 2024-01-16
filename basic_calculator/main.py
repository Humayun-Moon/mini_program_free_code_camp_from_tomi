print("Welcome to do the sum")
print()
def add(a,b):
    answer = a+b
    print(f"{a} and {b} addition is : {answer}")
def sub(a,b):
    answer = a - b
    print(f"{a} and {b} substraction is : {answer}")
def multi(a,b):
    answer = a * b
    print(f"{a} and {b} multiplication is : {answer}")
def div(a,b):
    answer = a/b
    print(f"{a} and {b} division is : {answer}") 

while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")

    choice = input("Enter your choice(q to quit): ").lower() 
    print("-------------------------------")
    
    if choice == "q":
        break
    elif choice == "a":
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        add(first_num,second_num)
    elif choice == "b":
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        sub(first_num,second_num)
    elif choice == "c":
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        multi(first_num,second_num)
    elif choice == "d":
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: ")) 
        div(first_num,second_num) 
    else:
        print("Try again with codition")   
        continue 
print("Bye, come again if you need")        
