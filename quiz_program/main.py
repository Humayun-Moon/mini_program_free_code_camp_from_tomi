quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    # Access the 'question' key, not ' question'
    print(value['question'])
    answer = input("Answer? ")

    # Compare answers in a case-insensitive manner
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])

    # Display score after each question
    print("Your score is: " + str(score))
    print("\n" + "-"*20 + "\n")

# Display final score and percentage
print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")
