import random

rps = random.randint(1, 3)

if rps == 1:
    computer_choice = "rock"
elif rps == 2:
    computer_choice = "paper"
elif rps == 3:
    computer_choice = "scissors"

user_choice = input("Rock Paper Scissors SHOOT! ")

print(f"Computer chose {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")