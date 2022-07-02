"""
Tic Tac Toe Player
"""

import math
from typing import List

X = "X"
O = "O"
EMPTY = None


def initial_state() -> List[List]:
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: List[List]) -> str:
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for row in board:
        for tile in row:
            if tile == X:
                xCount += 1
            elif tile == O:
                oCount += 1
    if xCount > oCount:
        return O
    else:
        return X


def actions(board: List[List]) -> set:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result


def result(board: List[List], action: tuple) -> List[List]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x, y = action
    if board[x][y] != EMPTY:
        raise Exception("Invalid move")
    # Make a copy of the board
    result = [row[:] for row in board]
    # Make the move on the copy
    result[x][y] = player(board)
    # Return the copy with the move
    return result


def winner(board: List[List]) -> str:
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2] 
    return None


def terminal(board: List[List]) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    # Check all rows
    win = winner(board)
    if win == X or win == O:
        return True
    # Check all columns
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board: List[List]) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board: List[List]) -> tuple:
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board: List[List]) -> int:
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board: List[List]) -> int:
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):
        return None
    if player(board) == X:
        for action in actions(board):
            if min_value(result(board, action)) == 1:
                return action
        for action in actions(board):
            if min_value(result(board, action)) == 0:
                return action
        for action in actions(board):
            if min_value(result(board, action)) == -1:
                return action
    else:
        for action in actions(board):
            if max_value(result(board, action)) == -1:
                return action
        for action in actions(board):
            if max_value(result(board, action)) == 0:
                return action
        for action in actions(board):
            if max_value(result(board, action)) == 1:
                return action
