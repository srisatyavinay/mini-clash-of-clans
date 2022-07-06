from colorama import Fore, Style, Back
from src.building import Building

class Hut(Building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 3
        self.height = 2
