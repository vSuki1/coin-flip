""" 
Program Name: Match Coins Game - Player Class
Disukhi Ahmed
Runs the game logic

"""

from player import Player

def main():
    player1 = Player("Player 1", 5)
    player2 = Player("Player 2", 5)

if __name__ == "__main__":
    main()

play = input("Do you want to toss the coins? y or n): ")

while (play == "y" or play == "Y"):

    player1.toss_coin()
    player2.toss_coin()

    