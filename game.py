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
            print("Type 'Hint' for a bonus hint!")
            guess = input("Enter your guess: ")
            if guess != "Hint":
                guess = int(guess)
        except ValueError:
            print("Please enter a number!")
        else:
            valid_guess = True
    return guess

def give_hint(numbers_guessed, answer):
    clg = float('-inf')
    chg = float('inf')

    for num in numbers_guessed:
        if answer > num > clg:
            clg = num
        if answer < num < chg:
            chg = num

    clg = clg if clg != float('-inf') else 1
    chg = chg if chg != float('inf') else 100

    if abs(answer - chg) < abs(answer - clg):
        print(f"The answer is closer to {chg} than {clg}")
    else:
        print(f"The answer is closer to {clg} than {chg}")

def game():
    print("Welcome to the Number Guessing Game!")
    print("You must guess the number between 1 and 100\n")

    difficulty = get_difficulty()
    difficulty_levels = {1: "Easy", 2: "Medium", 3: "Hard"}
    level = difficulty_levels[difficulty]
    print(f"Great! You have selected the {level} difficulty level.")

    guesses_total = (difficulty == 1) and 10 or (difficulty == 2) and 5 or (difficulty == 3) and 3
    guesses_used = 0
    numbers_guessed = []

    print("Let's start the game!\n")
    answer = randint(1, 100)
    start_time = time.time()

    while guesses_total - guesses_used > 0:
        guess = get_guess()

        if guess == "Hint":
            if guesses_used > 0:
                give_hint(numbers_guessed, answer)
            else:
                print("You can't use a hint on your first guess!")
            continue

        numbers_guessed.append(guess)
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