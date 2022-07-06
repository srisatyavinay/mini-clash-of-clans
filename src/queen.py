from colorama import Fore, Style, Back
from src.input import input_to
from src.king import King

class Queen(King):
    def __init__(self, x = 78, y = 30):
        super().__init__(x, y)
        self.width = 1
        self.height = 1
        self.wall = 25
        self.velocity = 1
        self.color = Back.LIGHTCYAN_EX+" "+Style.RESET_ALL
        self.full_health = 200
        self.health = self.full_health
        self.damage = 15
        self.aoex = 5
        self.aoey = 5

    def queen_attack(self, board, prev):
        y = [board.wall_list, board.hut_list, board.th_list, board.canon_list, board.wizard_list]
        if(prev == 0):
            posx = self.x - 2
            posy = self.y - 10
        elif(prev == 1):
            posx = self.x - 2
            posy = self.y + 6
        elif(prev == 2):
            posx = self.x - 10
            posy = self.y - 2
        elif(prev == 3):
            posx = self.x + 6
            posy = self.y - 2
        
        if((-1 in range(posx, posx + 5)) or (board.cols in range(posx, posx + 5)) or (-1 in range(posy, posy + 5)) or (board.rows in range(posy, posy + 5))):
            return

        for k in y:
            for l in k:
                ysame = 0
                xsame = 0
                at = 0
                al = 0
                for i in range(posy, posy + 5):
                    for j in range(l.y, l.y + l.height):
                        if(i == j):
                            ysame = 1
                            at = 1
                            break
                    if(at == 1):
                        break
                for i in range(posx, posx + 5):
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

