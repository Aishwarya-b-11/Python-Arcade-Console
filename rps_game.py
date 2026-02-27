# RPS - Rock, Paper, Scissors game - nested fucntion, golbal & local scope, closure, making game a module

import sys
import random
from enum import Enum


def rps(name):

    game_count = 0
    player_wins = 0
    computer_wins = 0

    def rps_game():
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal name

        game_count += 1

        class RPS(Enum):  # RPS - name to refer to 1, 2, 3
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Player choice
        playerchoice = input(
            f"\nHi {name}, choose and enter:\n1 - Rock,\n2 - Paper, or \n3 - Scissors\n")
        player = int(playerchoice)  # converting the str of input to int

        # checking if player has entered right choice from list
        if playerchoice not in ["1", "2", "3"]:
            print(
                f"Incorrect choice ❌\n{name}, please choose from: 1, 2, or 3.\n")
            return rps_game()

        # Computer choice
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        # Printing those choices
        print(f"{name}'s choice {str(RPS(player)).replace('RPS.', '').title()}")
        print(
            f"Python's choice {str(RPS(computer)).replace('RPS.', '').title()}\n")

        # Win or Lose
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal name
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name} won! 🎊"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name} won! 🎊"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} won! 🎊"
            elif player == computer:
                return "Draw match'🎭"
            else:
                computer_wins += 1
                return "Python wins 🐍\n Better luck next time\n"

        # closure so that we can have stack of game count + wins
        result = decide_winner(player, computer)
        print(result)

        print(f"Count of:")
        print(f"Game Round :{game_count}")
        print(f"{name}'s wins:{player_wins}")
        print(f"Python's wins:{computer_wins}\n")

        # Check if player wants to play again
        print("Want to play again?\n")
        while True:
            playagain = input("Enter:\nY - Yes,\nQ - Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue  # Anything other than y or q, ask for input again
            else:
                break

        if playagain.lower() == "y":
            return rps_game()
        else:
            print(
                f"\nThank you for playing, {name}! 😊\nGood Bye and see you next time! 👋")
            if __name__ == "__main__":
                sys.exit()  # if file is run as main, exit
            else:
                return

    return rps_game  # return the function result to the parent


# play = rps() -> creates an empty game before name is asked
if __name__ == "__main__":
    user_name = input(
        "\nEnter your name or press 'enter' to continue with name - Player: \n").title() or "Player"
    play = rps(user_name)
    play()
