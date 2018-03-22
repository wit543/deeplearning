from __future__ import print_function
import sys
sys.stdout.flush()
import json
import numpy as np
import random
from keras.models import model_from_json
# from rl import display_board
from env import Env


def display_board(state):
    print("| ", end='')
    for i in range(3):
        for j in range(3):
            idx = 3 * i + j
            if state[idx] == 1:
                print("O | ", end='')
            elif state[idx] == -1:
                print("X | ", end='')
            else:
                print('  | ', end='')
        print()
        if i != 2:
            print('| ', end="")
    print("-------------")

def check_if_ended(state):
    combinations = [
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((2, 0), (1, 1), (0, 2))
    ]

    for coordinates in combinations:
        letters = [state[3 * x + y] for x, y in coordinates]
        if sum(letters) == 3:
            return 1
        if sum(letters) == -3:
            return -1
    if state.count(0) == 0:
        return 2
    return 0


# if __name__ == "__main__":
def run():
    grid_size = 3
    with open("model/modelO_full.json", "r") as jfile:
        model1 = model_from_json(json.load(jfile))
    with open("model/modelX_full.json", "r") as jfile:
        model2 = model_from_json(json.load(jfile))
    model1.load_weights("model/modelO.h5")
    model2.load_weights("model/modelX.h5")
    env = Env(grid_size)
    print("Moves:")
    print("-------------")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print("-------------")

    while True:
        # print("1. AI starts")
        # print("2. Human starts")
        # print("3. Exit")
        while True:
            # choice = input()
            choice = 2
            if int(choice) in range(1, 4):
                break
        if int(choice) == 3:
            break
        board = [0 for x in range(9)]
        if int(choice) == 1:
            ai_turn = 0
            ai_piece = 1
            human_turn = 1
            human_piece = -1
            model = model1
        else:
            ai_turn = 1
            ai_piece = -1
            human_turn = 0
            human_piece = 1
            model = model2

        game_over = False
        turn = 0
        while not game_over:
            if turn % 2 == human_turn:
                print("\nYour Move [O] : ", end="")
                while True:
                    k = input()
                    if int(k) in range(1, 10) and board[int(k) - 1] == 0:
                        break
                board[int(k) - 1] = human_piece
                if check_if_ended(board) != 0:
                    game_over = True
            else:
                possible_actions = [i for i, e in enumerate(board) if e == 0]
                q = model.predict(np.reshape(board, (1, -1)))
                m = -1
                for i in possible_actions:
                    if q[0][i] > m:
                        action = i
                        m = q[0][i]
                if board.count(0) == 9:
                    action = random.randint(0, 8)
                print("AI plays [X] : " + str(action + 1) + '\n')
                board[action] = ai_piece
                print("-------------")
                display_board(board)
                # print("--------------------------")
                if check_if_ended(board) != 0:
                    game_over = True
            turn += 1

        print("\nGame Over . . .")
        if check_if_ended(board) == ai_piece:
            print("AI Won!\n")
        elif check_if_ended(board) == human_piece:
            print("You Won!\n")
        else:
            print("It's a draw!\n")
        print("-------------")
        display_board(board)

        # print("--------------------------")
