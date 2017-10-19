def check_win_vertical(board, j):
    iterations = len(board) - 1

    for i in range(iterations):
        if board[i][j] != board[i+1][j]:
            return False
    
    return True

def check_win_horizontal(board, i):
    iterations = len(board) - 1

    for j in range(iterations):
        if board[i][j] != board[i][j+1]:
            return False
    
    return True