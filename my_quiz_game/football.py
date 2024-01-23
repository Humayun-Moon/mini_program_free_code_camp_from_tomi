


def football(): 
        user_invest = float(input("How much amount want to invest: "))
        balance = 0
        
        score = 0
        question ={
              "q1":{
                    "qus": "The football size is like to see?",
                    "opt": "1. Square 2. Triangle 3. Long  4.Rounded ",
                    "ans": 4
                    
              },
              "q2":{
                    "qus": "The football size is like to see?",
                    "opt": "1. Square 2. Triangle 3. Long  4.Rounded ",
                    "ans": 4
                    
              },
              "q3":{
                    "qus": "The football size is like to see?",
                    "opt": "1. Square 2. Triangle 3. Long  4.Rounded ",
                    "ans": 4
                    
              },
              "q4":{
                    "qus": "The football size is like to see?",
                    "opt": "1. Square 2. Triangle 3. Long  4.Rounded ",
                    "ans": 4
                    
              },
              "q5":{
                    "qus": "The football size is like to see?",
                    "opt": "1. Square 2. Triangle 3. Long  4.Rounded ",
                    "ans": 4
                    
              },
        }

        for key,value in question.items():
            print(value['qus'])
            print(value['opt'])
            user_answer = int(input("Answer: "))
            if user_answer == value['ans']:
                  print("Correct Anserr") 
                  score += 1 
                  balance +=50
            else:
                  print("Incorrect")
                  print(f"Correct Answer is {value['ans']}")  
                  balance -= 50
        print("----Result Sheets ----")
        result = (score / 5) * 100 
        print(f"Your result is: {result}%") 

        print(f"You earned : {balance}")  
        
        print(f"You have remain balance: {user_invest + balance}")

        


              
