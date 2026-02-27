# GN - Guess number game

import sys
import random


def gn(name):
    game_count = 0
    player_wins = 0

    def guess_no():
        nonlocal game_count
        nonlocal player_wins
        nonlocal name

        game_count += 1

        playerchoice = input(
            f"\nHi {name}, from numbers 1 to 10, guess the number that I have selected\n")
        player = int(playerchoice)

        if player not in range(1, 11):
            print(
                f"Incorrect choice ❌\n{name}, Choose must be from: 1 to 10\n")
            return guess_no()

        computer = random.randint(1, 10)

        print(f"{name}'s choice: {player}")
        print(f"Python's choice : {computer}\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name} won! 🎊"
            else:
                return "Wrong guess. Better luck next time ❌\n"

        result = decide_winner(player, computer)
        print(result)

        print(f"Count of:")
        print(f"Game Round :{game_count}")
        print(f"{name}'s wins:{player_wins}")

        print("Want to guess again?")
        while True:
            playagain = input("Enter:\nY - Yes,\nQ - Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue  # Anything other than y or q, ask for input again
            else:
                break

        if playagain.lower() == "y":
            return guess_no()
        else:
            print(
                f"\nThank you for playing, {name}! 😊\nGood Bye and see you next time! 👋")
            if __name__ == "__main__":
                sys.exit()  # if file is run as main, exit
            else:
                return  # this part returns to the arcade, is the file is run from arcade not main

    return guess_no


if __name__ == "__main__":
    user_name = input(
        "\nEnter your name or press 'enter' to continue with name - Player: \n").title() or "Player"
    play = gn(user_name)
    play()
