print("Wecome for come to play.")
user_name = input("What's your name : ")
user_age = int(input("Your age: "))
user_email = input("Enter your Email: ")
user_balance = float(input("How much money you want to play: "))

def football():
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
              else:
                  print("Incorrect")
                  print(f"Correct Answer is {value['ans']}")        
              

def cricket():
      question ={
            "q1":{
                "qus":"Which contry explored the cricket game?",
                "opt":"1. Bangladeh 2.India 3. England 4. Pakistan",
                "ans": 3  
            },
            "q2":{
                "qus":"Which contry explored the cricket game?",
                "opt":"1. Bangladeh 2.India 3. England 4. Pakistan",
                "ans": 3  
            },
            "q3":{
                "qus":"Which contry explored the cricket game?",
                "opt":"1. Bangladeh 2.India 3. England 4. Pakistan",
                "ans": 3  
            },
            "q4":{
                "qus":"Which contry explored the cricket game?",
                "opt":"1. Bangladeh 2.India 3. England 4. Pakistan",
                "ans": 3  
            },
            "q5":{
                "qus":"Which contry explored the cricket game?",
                "opt":"1. Bangladeh 2.India 3. England 4. Pakistan",
                "ans": 3  
            },
            
      },
      
      

      for key,value in question.items():
              print(value['qus'])
              print(value['opt'])
              user_answer = int(input("Answer: "))
              if user_answer == value['ans']:
                    print("Correct Anserr")
              else:
                  print("Incorrect")
                  print(f"Correct Answer is {value['ans']}") 
      
game_options = ["1. Football" "2. Cricket"] 

for game in game_options:
    print(game, end=" ,")
print() 
user_choice = int(input("What game you want play: ")) 

if user_choice == 1:
      football()
elif user_choice == 2:
      cricket()      
else:
      print("Something else")
      print("Try again")      

