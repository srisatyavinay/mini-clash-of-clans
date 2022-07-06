from colorama import Fore, Style, Back
from src.building import Building
from src.king import sqr_dist

class Canon(Building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 3
        self.height = 3
        self.full_health = 80
        self.health = self.full_health
        self.damage = 10
        # self.color = Back.WHITE+" "+Style.RESET_ALL
        self.color = Back.CYAN+" "+Style.RESET_ALL
        self.color_flash = Back.LIGHTMAGENTA_EX+" "+Style.RESET_ALL

    def canon_attack(self, board):
        if(board.chosen == 0):
            y = [board.bar_list, board.king, board.arch_list]
        elif(board.chosen == 1):
            y = [board.bar_list, board.queen, board.arch_list]
        x = 0
        for t in y:
            for i in t:
                if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 5):
                    self.color = self.color2 = self.color3 = self.color_flash
                    i.decrease_health(self.damage)
                    if (i.health < 0):
                        t.remove(i)
                    x = 1
                    break
            if(x == 1):
                break
        if (x != 1):
            self.color = Back.CYAN+" "+Style.RESET_ALL
            self.color2 = Back.YELLOW+" "+Style.RESET_ALL
            self.color3 = Back.RED+" "+Style.RESET_ALL
