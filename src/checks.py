def check_win_vertical(board, j):
    for i in range(len(board) - 1):
        if board[i][j] != board[i+1][j]:
            return False
    
    return True

def check_win_horizontal(board, i):
    for j in range(len(board) - 1):
        if board[i][j] != board[i][j+1]:
            return False
    
    return True

def check_win_diagonal_lr(board):
    return board[0][0] is board[1][1] and board[0][0] is board[2][2]

def check_win_diagonal_rl(board):
    return board[2][0] is board[1][1] and board[2][0] is board[0][2]
