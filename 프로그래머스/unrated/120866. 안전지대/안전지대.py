def solution(board):
    x = len(board)
    y = len(board[0])
    
    bomb = [[0 for i in range(y+2)] for i in range(x+2)]
    
    for i in range(x):
        while(True):
            if sum(board[i]) == 0:
                break
            
            idx = board[i].index(1)
            board[i][idx] = 0
            
            bomb[i][idx:idx+3] = [1, 1, 1]
            bomb[i+1][idx:idx+3] = [1, 1, 1]
            bomb[i+2][idx:idx+3] = [1, 1, 1]
    bomb = bomb[1:len(bomb)-1]
    
    for i in range(x):
        bomb[i] = bomb[i][1:len(bomb[i])-1]
    return x * y - sum(sum( bomb, []))
