""" 
Program Name: Match Coins Game - Player Class
Disukhi Ahmed
Runs the game logic

"""

from player import Player

def main():
    player1 = Player("Player 1", 5)
    player2 = Player("Player 2", 5)


play = input("Do you want to toss the coins? y or n): ")

while (play == "y" or play == "Y"):

    player1.toss_coin()
    player2.toss_coin()

    side1 = player1.get_coin_side()
    side2 = player2.get_coin_side()

    print(f"{player1.get_name()} tossed {side1}")
    print(f"{player2.get_name()} tossed {side2}")

    if side1 == side2:
        player1.win_coin()
        player2.lose_coin()
    else:
        player1.lose_coin()
        player2.win_coin()

    print(f"{player1.get_name()} now has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} now has {player2.get_wallet()} coins.")

    play = input("do you want to toss the coins? y or n): ")