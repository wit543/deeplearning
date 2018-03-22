from __future__ import print_function
import sys
from random import randint
sys.stdout.flush()

pos_x = []
pos_o = []
pos_x_learn = []
pos_o_learn = []
def bot_turn():
    a = []
    for i in range(9):
        i = i + 1
        if i not in pos_x and i not in pos_o: 
            a.append(i)
    if len(a) == 0 or check_end_game(pos_x):
        return "END"
    else:
        index_a = randint(0,len(a)-1)
        pos_o.append(a[index_a])
        pos_o_learn.append(a[index_a])

def print_table(b):
    print("Your input position is : "+b)
    b = int(b) 
    pos_x.append(b)
    pos_x_learn.append(b)
    bot_turn()
    pos_x.sort()
    pos_o.sort()
    print("-------")
    p_i = 1
    p_io = 1
    co = 0
    coo = 0
    # print(pos_x)
    # print(pos_o)
    for i in range(3):
        print("|", end='')
        for j in range(3):
            if p_i == pos_x[co]:
                if co + 1 != len(pos_x):
                    co = co + 1
                print("x", end='')
            elif p_io == pos_o[coo]:
                if coo + 1 != len(pos_o):
                    coo = coo + 1
                print("o", end='')
            else:
                print(" ", end='')
            p_i = p_i + 1 
            p_io = p_io + 1 
            print("|", end='')
            b = b - 1
        print("")
    print("-------")

def end_game():
    if check_end_game(pos_x):
        print("X win . . .")
        return False
    if check_end_game(pos_o):
        print("O win . . .")
        return False
    return True

def check_end_game(p):
    if 1 in p and 2 in p and 3 in p:
        return True
    if 4 in p and 5 in p and 6 in p:
        return True
    if 7 in p and 8 in p and 9 in p:
        return True
    if 1 in p and 4 in p and 7 in p:
        return True
    if 2 in p and 5 in p and 8 in p:
        return True
    if 3 in p and 6 in p and 9 in p:
        return True
    if 1 in p and 5 in p and 9 in p:
        return True
    if 3 in p and 5 in p and 7 in p:
        return True








while end_game():
    pos_input = raw_input('Input position : ')
    if int(pos_input) in pos_x or int(pos_input) in pos_o:
            print("Invalid input . . . ")
    else: 
        print_table(pos_input)
        print(pos_x_learn)
        print(pos_o_learn)