from colorama import Fore, Style, Back
from src.building import Building

class Wall(Building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 2
        self.height = 1
        self.full_health = 30
        self.health = self.full_health
        self.color = Back.WHITE+" "+Style.RESET_ALL
        