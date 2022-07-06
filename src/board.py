from os import system
from colorama import Fore, Back, Style
from src.hut import Hut
from src.king import King
from src.townhall import Townhall
from src.wall import Wall
from src.canon import Canon
from src.barbarian import Barbarian
from src.archer import Archer
from src.queen import Queen
from src.wizard import Wizard

class Board():
    def __init__(self, chosen):
        self.cols = 80
        self.rows = 32
        self.chosen = chosen

        self.game_message = "In Level 1"

        self.border_width = 2
        self.border_top_height = 6

        self.bg_color = Back.BLACK+" "+Style.RESET_ALL
        self.border_color = Back.MAGENTA+" "+Style.RESET_ALL

        self.hut_list = [Hut(70, 10), Hut(60, 20), Hut(10, 18), Hut(15, 15), Hut(5, 26)]

        self.canon_list = [Canon(8, 8), Canon(40, 25)]

        self.wizard_list = [Wizard(20, 20), Wizard(60, 9)]

        self.wall_list = [Wall(70, 8), Wall(60, 18), Wall(10, 16), Wall(38, 14), Wall(40, 14), Wall(42, 14), Wall(44, 14)]

        self.bar_list = []

        self.arch_list = []

        self.bal_list = []

        if(self.chosen == 0):
            self.king = [King()]
        elif(self.chosen == 1):
            self.queen = [Queen()]
            
        self.th_list = [Townhall(40, 16)]

        self.output = [[self.border_color for i in range(self.cols + 2*self.border_width)] for j in range(self.rows + self.border_width + self.border_top_height)]
        self.present = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.output[i + self.border_top_height][j +self.border_width] = self.bg_color

        self.print_board()

    def print_board(self):
        
        system('clear')

        self.output = [[self.border_color for i in range(self.cols + 2*self.border_width)] for j in range(self.rows + self.border_width + self.border_top_height)]
        self.present = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.output[i + self.border_top_height][j +self.border_width] = self.bg_color

        for k in self.th_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    if(k.health > k.health2):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color
                    elif(k.health > k.health3):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color2
                    else:
                        self.output[i + self.border_top_height][j +self.border_width] = k.color3
                    self.present[i][j] = 1

        for k in self.hut_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    if(k.health > k.health2):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color
                    elif(k.health > k.health3):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color2
                    else:
                        self.output[i + self.border_top_height][j +self.border_width] = k.color3
                    self.present[i][j] = 1

        for k in self.wall_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    self.output[i + self.border_top_height][j +self.border_width] = k.color
                    self.present[i][j] = 1

        for k in self.canon_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    if(k.health > k.health2):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color
                    elif(k.health > k.health3):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color2
                    else:
                        self.output[i + self.border_top_height][j +self.border_width] = k.color3
                    self.present[i][j] = 1

        for k in self.wizard_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    self.output[i + self.border_top_height][j +self.border_width] = k.color
                    self.present[i][j] = 1

        for k in self.bar_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    if(k.health > k.health2):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color
                    elif(k.health > k.health3):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color2
                    else:
                        self.output[i + self.border_top_height][j +self.border_width] = k.color3

        for k in self.bal_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    self.output[i + self.border_top_height][j +self.border_width] = k.color
                    
        for k in self.arch_list:
            for i in range(k.y, k.y + k.height):
                for j in range(k.x, k.x + k.width):
                    self.output[i + self.border_top_height][j +self.border_width] = k.color

        if(self.chosen == 0):                         
            for k in self.king:
                for i in range(k.y, k.y + k.height):
                    for j in range(k.x, k.x + k.width):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color

            if(self.king != []):
                m = int(self.king[0].health/20)
            else:
                m = 0

            o = "King Health:"
            p = "Message:"+" "+self.game_message
            
            w = 0
            for k in p:
                self.output[4][w + self.border_width] = k
                w += 1

            e = 0
            for k in o:
                self.output[2][e + self.border_width] = k
                e += 1
            
            e += 1

            for k in range(1, 11):
                if (k <= m):
                    self.output[2][e + k + self.border_width - 1] = Back.GREEN+" "+Style.RESET_ALL
                else:
                    self.output[2][e + k + self.border_width - 1] = Back.RED+" "+Style.RESET_ALL
        elif(self.chosen == 1):
            for k in self.queen:
                for i in range(k.y, k.y + k.height):
                    for j in range(k.x, k.x + k.width):
                        self.output[i + self.border_top_height][j +self.border_width] = k.color

            if(self.queen != []):
                m = int(self.queen[0].health/20)
            else:
                m = 0

            o = "Queen Health:"
            p = "Message:"+" "+self.game_message
            
            w = 0
            for k in p:
                self.output[4][w + self.border_width] = k
                w += 1

            e = 0
            for k in o:
                self.output[2][e + self.border_width] = k
                e += 1
            
            e += 1

            for k in range(1, 11):
                if (k <= m):
                    self.output[2][e + k + self.border_width - 1] = Back.GREEN+" "+Style.RESET_ALL
                else:
                    self.output[2][e + k + self.border_width - 1] = Back.RED+" "+Style.RESET_ALL
        

        print("\n".join(["".join(i) for i in self.output]))
        # print("\n".join(["".join(str(i)) for i in self.present])
        # print(self.king[0].health)
