"""Functions used to check if there is a win on the board"""

def check_win_vertical(board, j):
    """Checks if there is a vertical win on the board"""

    for i in range(len(board) - 1):
        if board[i][j] != board[i+1][j]:
            return False
    
    return True

def check_win_horizontal(board, i):
    """Checks if there is a horizontal win on the board"""

    for j in range(len(board) - 1):
        if board[i][j] != board[i][j+1]:
            return False
    
    return True

def check_win_diagonal_lr(board):
    """Checks if there is a left-to-right diagonal win on the board"""

    return board[0][0] is board[1][1] and board[1][1] is board[2][2]

def check_win_diagonal_rl(board):
    """Checks if there is a right-to-left diagonal win on the board"""

    return board[2][0] is board[1][1] and board[1][1] is board[0][2]
