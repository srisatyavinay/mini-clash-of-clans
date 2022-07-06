# from colorama import Fore, Style, Back
# from src.barbarian import Barbarian
# from src.king import sqr_dist

# class Balloons(Barbarian):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.width = 2
#         self.height = 2
#         self.velocity = 2
#         self.color = Back.LIGHTBLUE_EX+" "+Style.RESET_ALL
#         self.full_health = 40
#         self.health = self.full_health
#         self.damage = 10
#         # self.range = 6

#     def move(self, board):
#         x = [board.canon_list, board.wizard_list]
#         y = [board.hut_list, board.th_list]
#         min = 1000
#         s = board.hut_list

#         x_is_empty = 0

#         if (x[0] != []):
#             near = x[0][0]
#         # elif (x[1] != []):
#         #     near = x[1][0]
#         elif (y[0] != []):
#             x_is_empty = 1
#             near = y[0][0]
#         else:
#             near = y[1][0]
#         if(x_is_empty == 0):
#             for j in x:
#                 for t in j:
#                     a = sqr_dist((self.y, self.x), (t.y, t.x))
#                     if a < min:
#                         min = a
#                         near = t
#                         s = j
#         else:
#             for j in y:
#                 for t in j:
#                     a = sqr_dist((self.y, self.x), (t.y, t.x))
#                     if a < min:
#                         min = a
#                         near = t
#                         s = j

#         # attacked = 0

#         # ysame = 0
#         # xsame = 0
#         # at = 0
#         # al = 0
#         # for i in range(self.y, self.y + self.height):
#         #     for j in range(near.y, near.y + near.height):
#         #         if(i == j):
#         #             ysame = 1
#         #             at = 1
#         #             break
#         #     if(at == 1):
#         #         break
#         # for i in range(self.x, self.x + self.width):
#         #     for j in range(near.x, near.x + near.width):
#         #         if(i == j):
#         #             xsame = 1
#         #             al = 1
#         #             break
#         #     if(al == 1):
#         #         break
#         # if(xsame == 1 and ysame == 1):
#         #     near.decrease_health(self.damage)
#         #     if(near.health <= 0):
#         #         s.remove(near)
#         #     attacked = 1

#         # if(attacked == 0):            
#         if(self.y < near.y and self.x < near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.y += self.velocity
#                 self.x += self.velocity
#         elif(self.y < near.y and self.x == near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x, self.x + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.y += self.velocity
#         elif(self.y < near.y and self.x > near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y + self.velocity, self.y + self.velocity + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x - self.velocity, self.x - self.velocity + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.y += self.velocity
#                 self.x -= self.velocity
#         elif(self.y == near.y and self.x < near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y, self.y + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.x += self.velocity
#         elif(self.y == near.y and self.x == near.x):
#             pass
#         elif(self.y == near.y and self.x > near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y, self.y + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x - self.velocity, self.x - self.velocity + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.x -= self.velocity
#         elif(self.y > near.y and self.x < near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x + self.velocity, self.x + self.velocity + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.y -= self.velocity
#                 self.x += self.velocity
#         elif(self.y > near.y and self.x == near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x, self.x + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.y -= self.velocity
#         elif(self.y > near.y and self.x > near.x):
#             attacked = 0
#             ysame = 0
#             xsame = 0
#             at = 0
#             al = 0
#             for i in range(self.y - self.velocity, self.y - self.velocity + self.height):
#                 for j in range(near.y, near.y + near.height):
#                     if(i == j):
#                         ysame = 1
#                         at = 1
#                         break
#                 if(at == 1):
#                     break
#             for i in range(self.x - self.velocity, self.x - self.velocity + self.width):
#                 for j in range(near.x, near.x + near.width):
#                     if(i == j):
#                         xsame = 1
#                         al = 1
#                         break
#                 if(al == 1):
#                     break
#             if(xsame == 1 and ysame == 1):
#                 near.decrease_health(self.damage)
#                 if(near.health <= 0):
#                     s.remove(near)
#                 attacked = 1
#             if(attacked == 0):
#                 self.y -= self.velocity
#                 self.x -= self.velocity

from colorama import Fore, Style, Back
from src.barbarian import Barbarian
from src.king import sqr_dist

class Balloons(Barbarian):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 2
        self.height = 2
        self.velocity = 2
        self.color = Back.LIGHTBLUE_EX+" "+Style.RESET_ALL
        self.full_health = 40
        self.health = self.full_health
        self.damage = 10
        # self.range = 6

    def move(self, board):
        x = [board.canon_list, board.wizard_list]
        y = [board.hut_list, board.th_list]
        min = 1000
        s = board.hut_list

        x_is_empty = 0

        if (x[0] != []):
            near = x[0][0]
        # elif (x[1] != []):
        #     near = x[1][0]
        elif (y[0] != []):
            x_is_empty = 1
            near = y[0][0]
        else:
            near = y[1][0]
        if(x_is_empty == 0):
            for j in x:
                for t in j:
                    a = sqr_dist((self.y, self.x), (t.y, t.x))
                    if a < min:
                        min = a
                        near = t
                        s = j
        else:
            for j in y:
                for t in j:
                    a = sqr_dist((self.y, self.x), (t.y, t.x))
                    if a < min:
                        min = a
                        near = t
                        s = j

        attacked = 0

        ysame = 0
        xsame = 0
        at = 0
        al = 0
        for i in range(self.y, self.y + self.height):
            for j in range(near.y, near.y + near.height):
                if(i == j):
                    ysame = 1
                    at = 1
                    break
            if(at == 1):
                break
        for i in range(self.x, self.x + self.width):
            for j in range(near.x, near.x + near.width):
                if(i == j):
                    xsame = 1
                    al = 1
                    break
            if(al == 1):
                break
        if(xsame == 1 and ysame == 1):
            near.decrease_health(self.damage)
            if(near.health <= 0):
                s.remove(near)
            attacked = 1

        if(attacked == 0):            
            if(self.y < near.y and self.x < near.x):
                self.y += self.velocity
                self.x += self.velocity
            elif(self.y < near.y and self.x == near.x):
                self.y += self.velocity
            elif(self.y < near.y and self.x > near.x):
                self.y += self.velocity
                self.x -= self.velocity
            elif(self.y == near.y and self.x < near.x):
                self.x += self.velocity
            elif(self.y == near.y and self.x == near.x):
                pass
            elif(self.y == near.y and self.x > near.x):
                self.x -= self.velocity
            elif(self.y > near.y and self.x < near.x):
                self.y -= self.velocity
                self.x += self.velocity
            elif(self.y > near.y and self.x == near.x):
                self.y -= self.velocity
            elif(self.y > near.y and self.x > near.x):
                self.y -= self.velocity
                self.x -= self.velocity

