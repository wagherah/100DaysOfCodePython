# # Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# name1 = name1.lower()
# name2 = name2.lower()
#
# t = name1.count("t") + name2.count("t")
# r = name1.count("r") + name2.count("r")
# u = name1.count("u") + name2.count("u")
# e = name1.count("e") + name2.count("e")
# l = name1.count("l") + name2.count("l")
# o = name1.count("o") + name2.count("o")
# v = name1.count("v") + name2.count("v")
#
# true_total = t + r + u + e
# love_total = l + o + v + e
#
# love_score = str(true_total) + str(love_total)
# love_score = int(love_score)
#
# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
#
# elif 50 > love_score > 40:
#     print(f"Your score is {love_score}, you are alright together.")
#
# else:
#     print(f"Your score is {love_score}.")
#
#


# Head Tails

# import random
#
# list_ = ["Heads", "Tails"]
#
# randomNumber = random.randint(0, 1)
#
# print(list_[randomNumber])

# Project

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
