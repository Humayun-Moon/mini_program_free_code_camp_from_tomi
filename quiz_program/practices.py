quiz ={
    "Question1":{
        "qus":"What is the capital city of Bangladesh? ",
        "option":"Gazipur Narayongonj  Dhaka Rangpur", 
        "ans": "Dhaka"
    },
    "Question2":{
        "qus":"What is the capital city of Bangladesh? ",
        "option":"Gazipur Narayongonj  Dhaka Rangpur", 
        "ans": "Dhaka"
    },
    "Question3":{
        "qus":"What is the capital city of Bangladesh? ",
        "option":"Gazipur Narayongonj  Dhaka Rangpur", 
        "ans": "Dhaka"
    },
    "Question4":{
        "qus":"What is the capital city of Bangladesh? ",
        "option":"Gazipur Narayongonj  Dhaka Rangpur", 
        "ans": "Dhaka"
    }
} 
   
score = 0
for key,value in quiz.items():
    print(value['qus'])
    print(value['option']) 
    answer = input("Answer: ").lower() 
    # print("-----------------------")
    if value['ans'].lower() == answer:
        print("Correct Answer")
        score +=1 
        
    else:
        print("Ahhha! Incorrect")
        print(f"Correct answer is: {value['ans']}")
        
    print(f"Your score is : {score}")
    print("\n" + "-"*20 + "\n") 

print("\n" + "-"*20 + "\n" )
print("---------Your Result-----------") 
percentage = (score/4) * 100 
print(f"Your accuracy: {percentage}%")





           