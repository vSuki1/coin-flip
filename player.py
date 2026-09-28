""" 
Program Name: Match Coins Game - Player Class
Disukhi Ahmed
Represents a player with a name, wallet of coins, and a Coin object.

"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.wallet = 20
        self.coin = Coin()
    def toss_coin(self):
        self.coin.toss()

    def get_coin_sideup(self):
        return self.coin.get_sideup()

    def win_coin(self):
        self.wallet += 1   

    def lose_coin(self):
        self.wallet -= 1

    def get_wallet(self):
        return self.wallet

    def get_name(self):
        return self.__name
    