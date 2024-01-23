import random 
name = input("What's Your Name: ")

def roll():
    dice_drowing = {
        1:(
            "Humayun_____fall_into_love_at_first_side_of_Khusbu________-----",
            "Khusbu_____fall_into_love_at_first_side_of_Humayun________-----",
            "They both want each others but can't express ",
        ),
        2:(
            "Humayun_____fall_into_love_at_first_side_of_Khusbu________-----",
            "They both want each others but can't express ",
            "Khusbu_____fall_into_love_at_first_side_of_Humayun________-----",
        ),
        3:(
            "Khusbu_____fall_into_love_at_first_side_of_Humayun________-----",
            "They both want each others but can't express ",
            "Humayun_____fall_into_love_at_first_side_of_Khusbu________-----",
        ),
        4:(
            "Humayun_____fall_into_love_at_first_side_of_Khusbu________-----",
            "Khusbu_____fall_into_love_at_first_side_of_Humayun________-----",
            "They both want each others but can't express ",
        ),
        5:(
            "Humayun_____fall_into_love_at_first_side_of_Khusbu________-----",
            "Khusbu_____fall_into_love_at_first_side_of_Humayun________-----",
            "They both want each others but can't express ",
        ),
        6:(
            "Humayun_____fall_into_love_at_first_side_of_Khusbu________-----",
            "Khusbu_____fall_into_love_at_first_side_of_Humayun________-----",
            "They both want each others but can't express ",
        ),
    }

    print(f"Hello, {name} welcome to dice rolling program") 
    urer_input = input("Do you want roll the dice (yes/no): ").lower()
    while urer_input == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print(f"Your dice {dice1} and {dice2}")
        print("\n".join(dice_drowing[dice1])) 
        print("-------------------------------")
        print("\n".join(dice_drowing[dice2])) 

        print("----------Result Sheets-------------")

        if dice1 == dice2:
            print("They both has accored")
        else:
            print("They couldn't accored with their concept")    

        urer_input = input("Do you again want to roll(yes/no) ") 
        print("")
roll()        
        

