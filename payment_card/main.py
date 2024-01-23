print("Welcome to the program of Payment per month your loan interest ")


def main():
    print("This is the monthly payment loan calculator")
    print("")

    principal = float(input("Enter your total loan amount: "))
    apr = float(input("Enter your annual interest rate :  "))
    years = int(input("Enter amount of years: "))

    monthly_interest_rate = apr/1200
    amount_of_months = years * 12
    monthly_pay = principal * monthly_interest_rate/(1 -(1 + monthly_interest_rate)**(-amount_of_months)) 

    print(monthly_pay)
main()    


    
