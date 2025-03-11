from random import randint
import time

def get_difficulty():
    difficulty = 0
    valid_difficulty = False
    while not valid_difficulty:
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)\n")
        difficulty = input("Enter your choice: ")
        try:
            difficulty = int(difficulty)
        except ValueError:
            print("Please enter a number!")
        else:
            if 0 < difficulty < 4:
                valid_difficulty = True

    return difficulty

def get_guess():
    guess = 0
    valid_guess = False
    while not valid_guess:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a number!")
        else:
            valid_guess = True
    return guess


def game():
    print("Welcome to the Number Guessing Game!")
    print("You must guess the number between 1 and 100\n")

    difficulty = get_difficulty()
    level = (difficulty == 1) and "Easy" or (difficulty == 2) and "Medium" or (difficulty == 3) and "Hard"
    print(f"Great! You have selected the {level} difficulty level.")

    guesses_total = (difficulty == 1) and 10 or (difficulty == 2) and 5 or (difficulty == 3) and 3
    guesses_used = 0

    print("Let's start the game!\n")

    start_time = time.time()
    answer = randint(1, 100)

    while guesses_total - guesses_used > 0:
        guess = get_guess()
        guesses_used += 1
        if guess == answer:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {guesses_used} attempts.")
            print(f"Time taken: {round(total_time,2)}s")
            break
        elif guess < answer:
            print(f"Incorrect! The number is greater than {guess}.")
            print(f"Attempts remaining: {guesses_total-guesses_used}")
        elif guess > answer:
            print(f"Incorrect! The number is less than {guess}.")
            print(f"Attempts remaining: {guesses_total - guesses_used}")
    else:
        print(f"Sorry, you didn't get it this time! The answer was {answer}")

while True:
    game()
    print("1. Play again")
    print("2. Quit game")
    while True:
        try:
            decision = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number")
        else:
            if decision < 1 or 2 < decision:
                continue
            else:
                break
    if decision == 2:
        break