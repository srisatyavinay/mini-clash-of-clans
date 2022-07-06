from colorama import Fore, Style, Back
from src.building import Building
from src.king import sqr_dist

class Barbarian(Building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 1
        self.height = 1
        self.velocity = 1
        self.color = Back.BLUE+" "+Style.RESET_ALL
        self.full_health = 40
        self.health = self.full_health
        self.damage = 5
        # self.velocity = 1

    def move(self, board):
        x = [board.hut_list, board.th_list, board.canon_list, board.wizard_list]
        y = [board.wall_list, board.hut_list, board.th_list, board.canon_list, board.wizard_list]
        min = 1000

        if (x[0] != []):
            i = x[0][0]
        elif (x[1] != []):
            i = x[1][0]
        else:
            i = x[2][0]
        for j in x:
            for t in j:
                a = sqr_dist((self.y, self.x), (t.y, t.x))
                if a < min:
                    min = a
                    i = t
        if(self.y < i.y and self.x < i.x):
            if(board.present[self.y + 1][self.x + 1] == 0):
                self.y += 1
                self.x += 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y + 1) >= l.y) and ((self.y + 1) < (l.y + l.height))) and (((self.x + 1) >= l.x) and ((self.x + 1) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y < i.y and self.x == i.x):
            if(board.present[self.y + 1][self.x] == 0):
                self.y += 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y + 1) >= l.y) and ((self.y + 1) < (l.y + l.height))) and (((self.x) >= l.x) and ((self.x) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y < i.y and self.x > i.x):
            if(board.present[self.y + 1][self.x - 1] == 0):
                self.y += 1
                self.x -= 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y + 1) >= l.y) and ((self.y + 1) < (l.y + l.height))) and (((self.x - 1) >= l.x) and ((self.x - 1) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y == i.y and self.x < i.x):
            if(board.present[self.y][self.x + 1] == 0):
                self.x += 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y) >= l.y) and ((self.y) < (l.y + l.height))) and (((self.x + 1) >= l.x) and ((self.x + 1) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y == i.y and self.x == i.x):
            ab = 0
            for k in y:
                for l in k:
                    if((((self.y) >= l.y) and ((self.y) < (l.y + l.height))) and (((self.x) >= l.x) and ((self.x) < (l.x + l.width)))):
                        l.decrease_health(self.damage)
                        if(l.health <= 0):
                            k.remove(l)
                        ab = 1
                        break
                if (ab == 1):
                    break
        elif(self.y == i.y and self.x > i.x):
            if(board.present[self.y][self.x - 1] == 0):
                self.x -= 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y) >= l.y) and ((self.y) < (l.y + l.height))) and (((self.x - 1) >= l.x) and ((self.x - 1) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y > i.y and self.x < i.x):
            if(board.present[self.y - 1][self.x + 1] == 0):
                self.y -= 1
                self.x += 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y - 1) >= l.y) and ((self.y - 1) < (l.y + l.height))) and (((self.x + 1) >= l.x) and ((self.x + 1) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y > i.y and self.x == i.x):
            if(board.present[self.y - 1][self.x] == 0):
                self.y -= 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y - 1) >= l.y) and ((self.y - 1) < (l.y + l.height))) and (((self.x) >= l.x) and ((self.x) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y > i.y and self.x > i.x):
            if(board.present[self.y - 1][self.x - 1] == 0):
                self.y -= 1
                self.x -= 1
            else:
                ab = 0
                for k in y:
                    for l in k:
                        if((((self.y - 1) >= l.y) and ((self.y - 1) < (l.y + l.height))) and (((self.x - 1) >= l.x) and ((self.x - 1) < (l.x + l.width)))):
                            l.decrease_health(self.damage)
                            if(l.health <= 0):
                                k.remove(l)
                            ab = 1
                            break
                    if (ab == 1):
                        break
        # pass
    
