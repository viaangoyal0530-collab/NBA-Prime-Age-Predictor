import random
user_num = int(input("What number do you want to end on? (1-_____)"))
user_guess = int(input(f"Guess a Number 1- {user_num}:"))
answer = random.randint(1, user_num)

while user_guess != answer:
    if user_guess > answer:
        print("Your guess is too high")
        user_guess = int(input(f"Guess a Number 1-{user_num}:"))
    elif user_guess < answer:
        print("Your guess is too low")
        user_guess = int(input(f"Guess a Number 1-{user_num}:"))
    else:
        print(f"Invalid input. Please enter a number between 1 and{user_num}.")
print("You guessed it right! The answer was", answer)