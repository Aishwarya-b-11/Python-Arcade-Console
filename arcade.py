import sys
from rps_game import rps
from gn_game import gn


def arcade_play(name='Player'):
    back_game = False

    while True:
        if back_game == True:
            print(f"\nHi {name}, welcome back to the Arcade.")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n3 = exit the Arcade\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"Incorrect selection\n")
            return arcade_play(name)

        back_game = True

        if playerchoice == "1":
            rps_play = rps(name)
            rps_play()
        elif playerchoice == "2":
            gn_play = gn(name)
            gn_play()
        else:
            print(f"Good Bye {name} and see you next time! 👋")
            sys.exit()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Personalized ")
    parser.add_argument('-n', '--name', metavar='name',
                        required=True, help='Name of the player')
    args = parser.parse_args()

    print(f"\nHi {args.name}, welcome to the Arcade")
    arcade_play(args.name)
