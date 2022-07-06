from colorama import Fore, Style, Back
from src.barbarian import Barbarian
from src.king import sqr_dist

class Archer(Barbarian):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 2
        self.height = 2
        self.velocity = 2
        self.color = Back.YELLOW+" "+Style.RESET_ALL
        self.full_health = 20
        self.health = self.full_health
        self.damage = 2.5
        self.range = 6

    def move(self, board):
        x = [board.hut_list, board.th_list, board.canon_list, board.wizard_list]
        y = [board.wall_list, board.hut_list, board.th_list, board.canon_list, board.wizard_list]
        min = 1000
        s = board.hut_list

        attacked = 0

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
                    s = j
        if(min <= self.range):
            i.decrease_health(self.damage)
            if(i.health <= 0):
                s.remove(i)
            attacked = 1
            
        if(self.y < i.y and self.x < i.x):
            present = 0
            for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                for j in range(self.x + self.velocity, self.x + self.velocity + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.y += self.velocity
                self.x += self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y < i.y and self.x == i.x):
            present = 0
            for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                for j in range(self.x, self.x + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.y += self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x , self.x + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y < i.y and self.x > i.x):
            present = 0
            for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                for j in range(self.x - self.velocity, self.x - self.velocity + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.y += self.velocity
                self.x -= self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x - self.velocity, self.x - self.velocity + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y == i.y and self.x < i.x):
            present = 0
            for i in range(self.y, self.y + self.height):
                for j in range(self.x + self.velocity, self.x + self.velocity + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.x += self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y, self.y + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y == i.y and self.x == i.x):
            if(attacked == 1):
                pass
            else:
                ab = 0
                for k in y:
                    for l in k:
                        ysame = 0
                        xsame = 0
                        at = 0
                        al = 0
                        for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
                            for j in range(l.y, l.y + l.height):
                                if(i == j):
                                    ysame = 1
                                    at = 1
                                    break
                            if(at == 1):
                                break
                        for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
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
                            ab = 1
                            break
                    if (ab == 1):
                        break
        elif(self.y == i.y and self.x > i.x):
            present = 0
            for i in range(self.y , self.y + self.height):
                for j in range(self.x - self.velocity, self.x - self.velocity + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.x -= self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y, self.y + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x - self.velocity, self.x - self.velocity + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y > i.y and self.x < i.x):
            present = 0
            for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
                for j in range(self.x + self.velocity, self.x + self.velocity + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.y -= self.velocity
                self.x += self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y > i.y and self.x == i.x):
            present = 0
            for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
                for j in range(self.x, self.x + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.y -= self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x, self.x + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        elif(self.y > i.y and self.x > i.x):
            present = 0
            for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
                for j in range(self.x - self.velocity, self.x - self.velocity + self.width):
                    if(board.present[i][j] == 1):
                        present = 1
                        break
            if(present == 0):
                self.y -= self.velocity
                self.x -= self.velocity
            else:
                if(attacked == 1):
                    pass
                else:
                    ab = 0
                    for k in y:
                        for l in k:
                            ysame = 0
                            xsame = 0
                            at = 0
                            al = 0
                            for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
                                for j in range(l.y, l.y + l.height):
                                    if(i == j):
                                        ysame = 1
                                        at = 1
                                        break
                                if(at == 1):
                                    break
                            for i in range(self.x - self.velocity, self.x - self.velocity + self.width):
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
                                ab = 1
                                break
                        if (ab == 1):
                            break
        # pass
