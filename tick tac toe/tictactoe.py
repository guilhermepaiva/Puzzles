import numpy as np
import pandas as pd

def init_board():
    return np.full((3,3), ' ')

def check_rules(board, line, column):
    line, column = int(line), int(column)
    if line not in [0, 1, 2]:
        print("line", line not in [0, 1, 2])
        print('You should enter line and column between 0 and 2! Pls, verify the rules!\n')
        print("[Rules: it is a 3x3 board and positoins starts with 0 and ends with 2 - for example: first posision is 0 0]\n")
        
        return False
    elif column not in [0, 1, 2]:
        print("column")
        print('You should enter line and column between 0 and 2! Pls, verify the rules!\n')
        print("[Rules: it is a 3x3 board and positoins starts with 0 and ends with 2 - for example: first posision is 0 0]\n")
        
        return False
    elif board[line][column] != ' ':
        print('This position has already a symbol. Try another position.\n')
        
        return False
    else:
        return True



def fill_board(board, line, column, symbol):
    board[line][column] = symbol
    return board
    
def verify_victory(board, symbol):
    if np.array_equal(board[0, 0:3], np.array([symbol, symbol, symbol])) or \
        np.array_equal(board[1, 0:3], np.array([symbol, symbol, symbol])) or \
            np.array_equal(board[2, 0:3], np.array([symbol, symbol, symbol])) or \
                np.array_equal(board[:, 0], np.array([symbol, symbol, symbol])) or \
                    np.array_equal(board[:, 1], np.array([symbol, symbol, symbol])) or \
                        np.array_equal(board[:, 2], np.array([symbol, symbol, symbol])) or \
                            np.array_equal(np.diagonal(board), np.array([symbol, symbol, symbol])) or \
                                np.array_equal(np.diagonal(np.fliplr(board)), np.array([symbol, symbol, symbol])):
                        return True, print(f'{symbol} WON!')
    else:
        return False, print()
    

if __name__ == "__main__":
    board = init_board()

    print("[Rules: it is a 3x3 board and positoins starts with 0 and ends with 2 - for example: first posision is 0 0]\n")

    symbols = ['X', 'O']
    i = 0
    while i < 9:
        print('Tell me the position (separated by space):') 

        line, column = input().split()
        
        while not check_rules(board, line, column):
            print('Tell me the position (separated by space):') 
            line, column = input().split()

        board = fill_board(board, int(line), int(column), symbols[i%2])
        print(board)
        result_game, phrase = verify_victory(board, symbols[i%2])
        if result_game:
            break
        print(15*"-")

        i += 1
        

        
    
    
    
    
    