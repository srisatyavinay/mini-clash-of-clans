from colorama import Fore, Style, Back
from src.canon import Canon
from src.king import sqr_dist

class Wizard(Canon):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = Back.LIGHTCYAN_EX+" "+Style.RESET_ALL
        self.color_flash = Back.LIGHTMAGENTA_EX+" "+Style.RESET_ALL

    def wizard_attack(self, board):
        x = 0
        if(board.chosen == 0):
            y = [board.bal_list, board.bar_list, board.king, board.arch_list]
        elif(board.chosen == 1):
            y = [board.bal_list, board.bar_list, board.queen, board.arch_list]
        for t in y:
            for i in t:
                if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 5):
                    self.color = self.color2 = self.color3 = self.color_flash
                    posx = i.x - 1
                    posy = i.y - 1
                    if((-1 in range(posx, posx + 3)) or (board.cols in range(posx, posx + 3)) or (-1 in range(posy, posy + 3)) or (board.rows in range(posy, posy + 3))):
                        i.decrease_health(self.damage)
                        if (i.health < 0):
                            t.remove(i)
                    else:
                        for k in y:
                            for l in k:
                                ysame = 0
                                xsame = 0
                                at = 0
                                al = 0
                                for i in range(posy, posy + 3):
                                    for j in range(l.y, l.y + l.height):
                                        if(i == j):
                                            ysame = 1
                                            at = 1
                                            break
                                    if(at == 1):
                                        break
                                for i in range(posx, posx + 3):
                                    for j in range(l.x, l.x + l.width):
                                        if(i == j):
                                            xsame = 1
                                            al = 1
                                            break
                                    if(al == 1):
                                        break
                                if(xsame == 1 and ysame == 1):
                                    l.decrease_health(self.damage)
                                    if(l.health <= 0):
                                        k.remove(l)
                    x = 1
                    break
            if(x == 1):
                break
        if (x != 1):
            self.color = Back.LIGHTCYAN_EX+" "+Style.RESET_ALL
            self.color2 = Back.YELLOW+" "+Style.RESET_ALL
            self.color3 = Back.RED+" "+Style.RESET_ALL
