"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countO = 0
    countX = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == O:
                countO += 1
            if board[row][col] == X:
                countX += 1

    if countX > countO:
        return O
    else:
        return X
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possibleActions.add((row, col))
    
    return possibleActions

    



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Not a valid action")
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)

    return board_copy

    



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if checkRow(board, X) or checkCol(board, X) or checkFirstDgl(board, X) or checkSecondDgl(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkFirstDgl(board, O) or checkSecondDgl(board, O):
        return O
    else:
        return None
    
    


def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    return False

def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    return False

def checkFirstDgl(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1

    if count == 3:
        return True
    else:
        return False
    
def checkSecondDgl(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1

    if count == 3:
        return True
    else:
        return False
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    

def maxValue(board):
    v = -math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v


def minValue(board):
    v = math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []

        for action in actions(board):
            plays.append([minValue(result(board, action)), action])
        
        return sorted(plays, key=lambda x: x[0], reverse = True)[0][1]
    elif player(board) == O:
        plays = []

        for action in actions(board):
            plays.append([maxValue(result(board, action)), action])
        
        return sorted(plays, key=lambda x: x[0])[0][1]


    raise NotImplementedError

