def cricket():
    user_invest = float(input("How much amount want to invest: "))
    balance = 0
    score = 0 
    question = {
        "q1": {
            "qus": "Which country explored the cricket game?",
            "opt": "1. Bangladesh 2. India 3. England 4. Pakistan",
            "ans": 3  
        },
        "q2": {
            "qus": "Which country explored the cricket game?",
            "opt": "1. Bangladesh 2. India 3. England 4. Pakistan",
            "ans": 3  
        },
        "q3": {
            "qus": "Which country explored the cricket game?",
            "opt": "1. Bangladesh 2. India 3. England 4. Pakistan",
            "ans": 3  
        },
        "q4": {
            "qus": "Which country explored the cricket game?",
            "opt": "1. Bangladesh 2. India 3. England 4. Pakistan",
            "ans": 3  
        },
        "q5": {
            "qus": "Which country explored the cricket game?",
            "opt": "1. Bangladesh 2. India 3. England 4. Pakistan",
            "ans": 3  
        },
    }

    for key, value in question.items():
        print(value['qus'])
        print(value['opt'])
        user_answer = int(input("Answer: "))
        if user_answer == value['ans']:
            print("Correct Answer") 
            score += 1 
            balance += 50
        else:
            print("Incorrect")
            print(f"Correct Answer is {value['ans']}") 
            balance -= 50

    print("----Result Sheets ----")
    result = (score / 5) * 100 
    print(f"Your result is: {result}%") 
    print(f"You earned: {balance}")  
    print(f"You have remaining balance: {user_invest + balance}")             

# Call the function to run the cricket quiz

