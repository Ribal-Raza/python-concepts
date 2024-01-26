import sys
import random
from enum import Enum

# input() takes a string argument and prints it in cli, then waits for user input.
# It takes the value of user input and then assigns it to variable it has been set to
# value = input("Enter a value:\t")
# print(value)

# Creating a game rock paper scissors


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    print("")
    playerschoice = input("Enter... \n1 for Rock⛰, \n2 for Paper📃, \n3 for Scissors✂\n")
    player = int(playerschoice)
    if player < 1 or player > 3:
        sys.exit(print("Please chose from 1 to 3 "))

    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("You chose " + playerschoice + ".")
    print("Python chose " + computerchoice + ".")

    if player == 1 and computer == 3:
        print("You Win! 🏆")
    elif player == 2 and computer == 1:
        print("You Win! 🏆")
    elif player == 3 and computer == 2:
        print("You Win! 🏆")
    elif player == computer:
        print("Game Tie!👍")
    else:
        print("Python🐍 Wins! 🏆")

    playagain = input("Do you want to play again? Y/N \t")
    if playagain == "Y" or playagain == 'y':
        continue
    elif playagain == "N" or playagain=='n':
        print("See you next time!👋")
        playagain=False

    
