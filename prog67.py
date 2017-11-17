def generateMoves(color,board):
    import copy
    newboard = copy.deepcopy(board)
    b = board
    move = []
    for i in range(0,len(b)):
        for j in range(0,len(b[0])):
            newboard = copy.deepcopy(board)
            b = board
            if color == 1 and board[i][j] == color:
                if (i == 0) and (j == (len(b[0])-1)):
                    if  b[i+1][j] == 0:
                        newboard[i+1][j] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                    
                    if b[i+1][j-1] == 2:
                        newboard[i+1][j-1] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                        
                if i == 0 and j == 0:
                    if  b[i+1][j] == 0:
                        newboard[i+1][j] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                        
                        
                    if b[i+1][j+1] == 2:
                        newboard[i+1][j+1] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                elif i in range(0,len(b)) and j in range(0,len(b[0])-1):
                    if b[i+1][j] == 0:
                        newboard[i+1][j] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                        
                        
 
                    if b[i+1][j-1] == 2:
                        newboard[i+1][j-1] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                        
                
                    if b[i+1][j+1] == 2:
                        newboard[i+1][j+1] = board[i][j]
                        newboard[i][j] = 0
                        move = move + [newboard]
                        newboard = copy.deepcopy(board)
                        b = board
                        
                        
                    
            elif color == 2 and board[i][j] == color:
                    if i == len(b)-1 and j == 0:
                        if b[i-1][j] == 0:
                            newboard[i-1][j] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
                            
 
                        if b[i-1][j+1] == 1:
                            newboard[i+1][j+1] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
                            
                        
                    if i == len(b) - 1 and j == len(b[0])-1:
                        if board[i-1][j] == 0:
                            newboard[i-1][j] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
                            
                        if board[i-1][j-1] == 1:
                            newboard[i-1][j-1] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
                           
                        
                    else:
                        if b[i-1][j] == 0:
                            newboard[i-1][j] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
                            
                        if b[i-1][j+1] == 1:
                            newboard[i-1][j+1] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
                        if b[i-1][j-1] == 1:
                            newboard[i-1][j-1] = board[i][j]
                            newboard[i][j] = 0
                            move = move + [newboard]
                            newboard = copy.deepcopy(board)
                            b = board
    return move
            
def chooseBestMove(color, mlist):
    index = 0
    difference = 0
    maximum = 0
    countblack = 0
    countwhite = 0
    if color == 1:
        for  x in range(0,len(mlist)):
            for y in range(0,len(mlist[0])):
                for z in mlist[x][y]:
                    if z == color:
                        countblack += 1
                    if z == 2:
                        countwhite += 1
        difference = countblack - countwhite
        if difference >= maximum:
            maximum = difference
            index = index + 1
            print(mlist[index])
            
                        
    if color == 2:
        for x in range(0,len(mlist)):
            for y in range(0,len(mlist[0])):
                for z in mlist[x][y]:
                    if z == color:
                        countwhite += 1
                    if z == 1:
                        countblack += 1
        difference = countwhite - countblack
        if difference >= maximum:
            maximum = difference
            index = index + 1
            print(mlist[index])
    return
                    
