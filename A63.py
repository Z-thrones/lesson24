import random
while True:
    user_action = input("Enter Rock,Paper, or Scissors: ")
    posible_actios = "Rock , Paper , Scissiors"
    computer_action = random.choice(posible_actios)
    print(f"The user input was " , user_action , " and the computer action was " , computer_action)
    if user_action == computer_action:
        print("Its a tie")
    elif user_action == "Rock" and computer_action == "Scissors":
        print("User wins")
    elif user_action == "Scissors" and computer_action == "Paper":
        print("User wins")
    elif user_action == "Paper" and computer_action == "Rock":
        print("User wins")
    else:
        print("Computer wins")