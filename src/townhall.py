from colorama import Fore, Style, Back
from src.building import Building

class Townhall(Building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 4
        self.height = 3
        self.full_health = 100
        self.health = self.full_health
