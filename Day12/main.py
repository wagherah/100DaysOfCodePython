# Number Guessing Game

import random
# from this import d
modes = {"Easy": 10, "Hard": 5}

def game():

    print("Welcome to Number Guessing Game!")

    computer_guess = random.randint(1, 100)
    print("I am thinking of a number between 1 to 100.")



    difficulty_level = input("Choose a difficult. Type 'Easy' or 'Hard':")

    logic(computer_guess, difficulty_level)

    replay = input("Do you wan to play again? 'Y' or 'N'")
    if replay == "Y":
        game()
    else:
        exit()


def logic(computer_guess, difficulty_level):

    remaining_guesses = modes[difficulty_level]

    while remaining_guesses > 0:
        print(f"You have {remaining_guesses} attempts remaining to guess the number")
        user_guess = int(input("Make a guess. "))

        if user_guess == computer_guess:
            print("You guessed it right. You Won")
            remaining_guesses -= 1
            return

        elif user_guess > computer_guess:
            print("Guess too high.")
            remaining_guesses -= 1

        elif user_guess < computer_guess:
            print("Guess too low.")
            remaining_guesses -= 1

    print("Guesses end. You loss")




game()


