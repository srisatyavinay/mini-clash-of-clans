from colorama import Fore, Style, Back

class Building():
    def __init__(self, x, y):
        self.width = 1
        self.height = 1
        self.color = Back.GREEN+" "+Style.RESET_ALL
        self.color2 = Back.YELLOW+" "+Style.RESET_ALL
        self.color3 = Back.RED+" "+Style.RESET_ALL
        self.full_health = 50
        self.health = self.full_health
        self.health2 = int(self.full_health/2)
        self.health3 = int(self.full_health/4)
        self.x = x
        self.y = y

    def decrease_health(self, val):
        self.health = self.health - val
        
    def get_health(self):
        return self.health
