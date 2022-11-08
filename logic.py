# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import math

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(row)

def print_board_positions(board):
    print("Board square positions:")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")

    # for i in range(1,10):
    #     if board[i-1] == None:
    #         print(i)
        # else print (board[i])


def update_board(board, index, turn):

    # print(index)
    # print(type(int(index)))
    index = int(index)

    assert index > 0 and index < 10
    
    if (index < 1  or index > 9):
        print("Sorry, enter a number between 1 and 9")


    index = index - 1
    board_x = int(index / 3)
    board_y = math.ceil(index % 3)
    if(board[board_x][board_y] == None):
        board[board_x][board_y] = turn
    else:
        print("Choose an empty location! This slot is taken")
        input_index = input("\nChoose a position to add your symbol: ")
        update_board(board, input_index, turn)


    return board


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    if(board[0][0] == board[0][1] == board[0][2]):
        winner = board[0][0]
        # print(winner + (" first row"))
        
    elif(board[1][0] == board[1][1] == board[1][2]):
        winner = board[1][0]
        # print(winner + (" middle row"))

    elif(board[2][0] == board[2][1] == board[2][2]):
        winner = board[2][0]
        # print(winner + (" last row"))

    elif((board[0][0] == board[1][1] == board[2][2])):
        winner = board[0][0]
        # print(winner + (" left diagonal"))
        
    elif((board[2][0] == board[1][1] == board[0][2])):
        winner = board[2][0]
        # print(winner + (" right diagonal"))
    
    elif((board[0][0] == board[1][0] == board[2][0])):
        winner = board[0][0]
        # print(winner + (" first column"))
        
    elif((board[0][1] == board[1][1] == board[2][1])):
        winner = board[0][1]
        # print(winner + (" middle column"))
    
    elif((board[0][2] == board[1][2] == board[2][2])):
        winner = board[0][2]
        # print(winner + (" last column"))
    else:
        winner = None
        
    return winner


def other_player(player):
    """Given the character for a player, returns the other player."""
    assert player != None
    if player == 'X':
        return 'O'  # FIXME
    else:
        return 'X'

    