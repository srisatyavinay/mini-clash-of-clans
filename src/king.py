from colorama import Fore, Style, Back
from src.input import input_to
from math import sqrt
from src.building import Building

def sqr_dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

class King(Building):
    def __init__(self, x = 78, y = 30):
        super().__init__(x, y)
        self.width = 1
        self.height = 1
        self.wall = 25
        self.velocity = 1
        self.color = Back.RED+" "+Style.RESET_ALL
        self.full_health = 200
        self.health = self.full_health
        self.damage = 20

    def move(self, board, char):
        # char = input_to()
        if(char == 'd'):
            if((self.x+self.width+self.velocity-2) < (board.cols-1) and board.present[self.y][self.x + self.velocity] == 0):
                self.x = self.x+self.velocity
        elif(char == 'a'):
            if(self.x-self.velocity+1 > 0 and board.present[self.y][self.x - self.velocity] == 0):
                self.x = self.x-self.velocity
        elif(char == 'w'):
            if(self.y-self.velocity+1 > 0 and board.present[self.y - self.velocity][self.x] == 0):
                self.y = self.y-self.velocity
        elif(char == 's'):
            if((self.y+self.height+self.velocity-2) < (board.rows-1) and board.present[self.y + self.velocity][self.x] == 0):
                self.y = self.y+self.velocity
        # return char
    
    def king_attack(self, board):
        for i in board.wall_list:
            if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 3):
                i.decrease_health(self.damage)
                if (i.health <= 0):
                    board.wall_list.remove(i)
        for i in board.canon_list:
            if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 3):
                i.decrease_health(self.damage)
                if (i.health <= 0):
                    board.canon_list.remove(i)
        for i in board.hut_list:
            if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 3):
                i.decrease_health(self.damage)
                if (i.health < 0):
                    board.hut_list.remove(i)
        for i in board.th_list:
            if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 3):
                i.decrease_health(self.damage)
                if (i.health < 0):
                    board.th_list.remove(i)
        for i in board.wizard_list:
            if(sqr_dist((i.y, i.x), (self.y, self.x)) <= 3):
                i.decrease_health(self.damage)
                if (i.health < 0):
                    board.wizard_list.remove(i)
