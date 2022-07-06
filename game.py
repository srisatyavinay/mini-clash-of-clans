from src.board import Board
from src.input import input_to
from src.barbarian import Barbarian
from src.archer import Archer
from src.balloons import Balloons
from src.hut import Hut
from src.king import King
from src.townhall import Townhall
from src.wall import Wall
from src.canon import Canon
from src.queen import Queen
from src.wizard import Wizard

chosen = input("Choose between King(0) and Queen(1): ")

chosen = int(chosen)

board = Board(chosen)

board.print_board()

a = [6, 6, 3]

level = 1

num_level = [1, 1]

prev = 0

while(True):
    #check game over
    if(chosen == 0):
        if(board.bar_list == [] and board.king == [] and a == [0, 0, 0]):
            board.game_message = "Defeat (Game over)"
            board.print_board()
            break
    elif(chosen == 1):
        if(board.bar_list == [] and board.queen == [] and a == [0, 0, 0]):
            board.game_message = "Defeat (Game over)"
            board.print_board()
            break
    if(board.hut_list == [] and board.th_list == [] and board.canon_list == [] and board.wizard_list == [] and level == 1 and num_level[0] == 1):
        level += 1
        num_level[0] -= 1
        board.game_message = "Level 1 completed"
        board.print_board()
        board.game_message = "In Level 2"
        a = [6, 6, 3]
        board.hut_list = [Hut(70, 10), Hut(60, 20), Hut(10, 18), Hut(15, 15), Hut(5, 26)]
        board.canon_list = [Canon(8, 8), Canon(40, 25), Canon(22, 11)]
        board.wizard_list = [Wizard(20, 20), Wizard(60, 9), Wizard(65, 20)]
        board.wall_list = [Wall(70, 8), Wall(60, 18), Wall(10, 16), Wall(38, 14), Wall(40, 14), Wall(42, 14), Wall(44, 14)]
        board.bar_list = []
        board.arch_list = []
        board.bal_list = []
        if(board.chosen == 0):
            board.king = [King()]
        elif(board.chosen == 1):
            board.queen = [Queen()]
        board.th_list = [Townhall(40, 16)]
    if(board.hut_list == [] and board.th_list == [] and board.canon_list == [] and board.wizard_list == [] and level == 2 and num_level[1] == 1):
        level += 1
        num_level[1] -= 1
        board.game_message = "Level 2 completed"
        board.print_board()
        board.game_message = "In Level 3"
        a = [6, 6, 3]
        board.hut_list = [Hut(70, 10), Hut(60, 20), Hut(10, 18), Hut(15, 15), Hut(5, 26)]
        board.canon_list = [Canon(8, 8), Canon(40, 25), Canon(22, 11), Canon(45, 3)]
        board.wizard_list = [Wizard(20, 20), Wizard(60, 9), Wizard(65, 20), Wizard(30, 15)]
        board.wall_list = [Wall(70, 8), Wall(60, 18), Wall(10, 16), Wall(38, 14), Wall(40, 14), Wall(42, 14), Wall(44, 14)]
        board.bar_list = []
        board.arch_list = []
        board.bal_list = []
        if(board.chosen == 0):
            board.king = [King()]
        elif(board.chosen == 1):
            board.queen = [Queen()]
        board.th_list = [Townhall(40, 16)]
    if(board.hut_list == [] and board.th_list == [] and board.canon_list == [] and board.wizard_list == [] and level == 3):
        board.game_message = "Victory (Game over)"
        board.print_board()
        break
    check = input_to()
    if(chosen == 0):
        if(check == 'w' or check == 's' or check == 'a' or check == 'd'):
            if(board.king != []):
                board.king[0].move(board, check)
        elif(check == ' '):
            if(board.king != []):
                board.king[0].king_attack(board)
    elif(chosen == 1):
        if(check == 'w'):
            if(board.queen != []):
                board.queen[0].move(board, check)
                prev = 0
        elif(check == 's'):
            if(board.queen != []):
                board.queen[0].move(board, check)
                prev = 1
        elif(check == 'a'):
            if(board.queen != []):
                board.queen[0].move(board, check)
                prev = 2
        elif(check == 'd'):
            if(board.queen != []):
                board.queen[0].move(board, check)
                prev = 3
        elif(check == ' '):
            if(board.queen != []):
                board.queen[0].queen_attack(board, prev)
    if(check == 'b'):
        if(a[0] > 0):
            a[0] -= 1
            board.bar_list.append(Barbarian(1, 16))
    elif(check == 'y'):
        if(a[0] > 0):
            a[0] -= 1
            board.bar_list.append(Barbarian(40, 1))
    elif(check == 'n'):
        if(a[0] > 0):
            a[0] -= 1
            board.bar_list.append(Barbarian(78, 16))
    elif(check == 'c'):
        if(a[1] > 0):
            a[1] -= 1
            board.arch_list.append(Archer(1, 16))
    elif(check == 't'):
        if(a[1] > 0):
            a[1] -= 1
            board.arch_list.append(Archer(40, 1))
    elif(check == 'v'):
        if(a[1] > 0):
            a[1] -= 1
            board.arch_list.append(Archer(78, 16))
    elif(check == 'z'):
        if(a[2] > 0):
            a[2] -= 1
            board.bal_list.append(Balloons(1, 16))
    elif(check == 'e'):
        if(a[2] > 0):
            a[2] -= 1
            board.bal_list.append(Balloons(40, 1))
    elif(check == 'x'):
        if(a[2] > 0):
            a[2] -= 1
            board.bal_list.append(Balloons(78, 16))
    elif(check == 'h'):
        for i in board.bar_list:
            if((i.health * 1.5) < i.full_health):
                i.health *= 1.5
            else:
                i.health = i.full_health
        for i in board.bal_list:
            if((i.health * 1.5) < i.full_health):
                i.health *= 1.5
            else:
                i.health = i.full_health
        for i in board.arch_list:
            if((i.health * 1.5) < i.full_health):
                i.health *= 1.5
            else:
                i.health = i.full_health
        if(chosen == 0):
            for i in board.king:
                if((i.health * 1.5) < i.full_health):
                    i.health *= 1.5
                else:
                    i.health = i.full_health
        elif(chosen == 1):
            for i in board.queen:
                if((i.health * 1.5) < i.full_health):
                    i.health *= 1.5
                else:
                    i.health = i.full_health
    elif(check == 'r'):
        for i in board.bar_list:
            i.damage *= 2
            # i.velocity *= 2
        for i in board.bal_list:
            i.damage *= 2
            # i.velocity *= 2
        for i in board.arch_list:
            i.damage *= 2
            # i.velocity *= 2
        if(chosen == 0):
            for i in board.king:
                i.damage *= 2
                # i.velocity *= 2
        elif(chosen == 1):
            for i in board.queen:
                i.damage *= 2
                # i.velocity *= 2
    elif(check == 'q'):
        break
    for i in board.canon_list:
        i.canon_attack(board)
    for i in board.wizard_list:
        i.wizard_attack(board)
    for i in board.bar_list:
        i.move(board)
    for i in board.arch_list:
        i.move(board)
    for i in board.bal_list:
        i.move(board)
    board.print_board()
