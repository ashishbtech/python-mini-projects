import random

print("Welcome to Rock Paper Scissors!")

choices = ["rock", "paper", "scissors"]

while True:

    user = input("\nEnter rock, paper, scissors or q to quit: ").lower()

    if user == "q":
        print("Thanks for playing!")
        break

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a draw!")

    elif user == "rock" and computer == "scissors":
        print("You win!")

    elif user == "paper" and computer == "rock":
        print("You win!")

    elif user == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("Computer wins!")