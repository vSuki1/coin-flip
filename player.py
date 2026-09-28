""" 
Program Name: Match Coins Game - Player Class
Disukhi Ahmed
Represents a player with a name, wallet of coins, and a Coin object.

"""

from coin import Coin

class Player:
    def __init__(self, name, wallet):
        self.__name = name
        self.wallet = wallet
        self.coin = Coin()
    