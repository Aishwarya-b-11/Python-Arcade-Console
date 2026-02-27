# RPS - Rock, Paper, Scissors game with while loop/ This is simple prototype
# Problem - anything other than q also quits, no closure

import sys
import random
from enum import Enum


class RPS(Enum):  # RPS - name to refer to 1, 2, 3
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    # Player choice
    print("")
    playerchoice = input(
        "Choose and enter your option:\n1 - Rock,\n2 - Paper, or \n3 - Scissors\n")
    player = int(playerchoice)  # converting the str of input to int
    print("")

    # checking if player has entered right choice from list
    if player < 1 or player > 3:
        sys.exit("Your choice is incorrect.\nChoise must be either 1, 2, or 3.")

    # Computer choice
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    # Printing those choices
    print("Your choice " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python's choice " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    # Win or Lose
    if player == 1 and computer == 3:
        print("You won! 🎊")
    elif player == 2 and computer == 1:
        print("You won! 🎊")
    elif player == 3 and computer == 2:
        print("You won! 🎊")
    elif player == computer:
        print("Draw match'🎭")
    else:
        print("Python wins 🐍\nBetter luck next time")
    print("")

    # Check if player wants to play again
    playagain = input(
        "Want to play again?, enter:\nY - Yes or \nQ - Quit \n\n")
    print("")
    if playagain.lower() == "y":
        continue
    else:
        print("Thank you for playing! 😊\n")
        playagain = False  # to stop the game while loop

sys.exit("Good Bye and see you next time! 😊")
