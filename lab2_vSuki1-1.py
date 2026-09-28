""" 
Program Name: Match Coins Game - Player Class
Disukhi Ahmed
Runs the game logic

"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    
    play = input("Do you want to toss the coins? y or n): ")

    while (play == "y" or play == "Y"):

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_sideup()
        side2 = player2.get_coin_sideup()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            print("Both players tossed the same side")
            player1.win_coin()
            player2.lose_coin()
        else:
            print("Both players tossed different sides")
            player1.lose_coin()
            player2.win_coin()

        print(f"{player1.get_name()} now has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} now has {player2.get_wallet()} coins.")

        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("GAME OVER")
            break
       
        play = input("do you want to toss the coins? y or n): ")

if __name__ == "__main__":
    main()