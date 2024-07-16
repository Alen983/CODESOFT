import random

def game():
    choice = {1:"Rock" , 2:"Paper", 3:"Scissors"}
    print("Welcome to rock paper scissors")
    print("Choose any of the following")
    print("Just enter 1,2 or 3")
    print("1.Rock")
    print("2.paper")
    print("3.Scissors")


    user_choice = int(input("Enter your choice "))
    if user_choice == 1:
        u_choice = choice[1]
    elif user_choice==2:
        u_choice = choice[2]
    elif user_choice ==3:
        u_choice = choice[3] 
    else:
        print("Invalid number entered")
        exit()

    print(f"You played:{u_choice}")

    computer_choice = random.choice(list(choice.values()))
    print(f"computer plays:{computer_choice}")


    if u_choice == computer_choice:
        print("Tie")
    elif (u_choice == "Rock" and computer_choice == "Scissors") or \
        (u_choice == "Paper" and computer_choice=="Rock") or \
        (u_choice == "Scissors" and computer_choice == "Paper"):
        print("You win")
    else:
        print("Computer Wins")

while True:
    game()
    restart = input("Do you want to play again?(Y/N)").lower()
    if restart == "n":
        exit()


