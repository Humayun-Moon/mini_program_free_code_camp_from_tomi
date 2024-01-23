import random 






def roll_dice():
    dice_drawing = {
        1:(
            "-----------",
            "[-Humayun--]",
            "[-Khusbu---]"
        ),
        2:(
            "-----------",
            "[-Khusbu---]",
            "[-Humayun--]",
        ),
        3:(
            "-----------",
            "[-Humayun--]",
            "[-Khusbu---]"
        ),
        4:(
            "-----------",
            "[-Khusbu---]",
            "[-Humayun--]",
        ),
        5:(
            "-----------",
            "[-Khusbu---]",
            "[-Humayun--]",
        ),
        6:(
            "-----------",
            "[-Khusbu---]",
            "[-Humayun--]",
        ),

    }


    roll = input("Do you want to roll the dice(yes/no)").lower()
    while roll == "yes":
        dice1 = random.randint(1,6) 
        dice2 = random.randint(1,6) 

        print(f"dice rolled: {dice1} and {dice2}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll =input("Roll again? (yes/no): ") 

           
roll_dice() 


