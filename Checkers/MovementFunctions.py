def moveFR(x,y, playerNum):
    if x == 0 or y == 7:
        print("invalid move")
        return 0
    grid[x][y] = 0
    x=x-1
    y=y+1
    grid[x][y] = playerNum
    return

def moveFL(x,y, playerNum):
    if x == 0 or y == 0:
        print("invalid move")
        return 0
    grid[x][y] = 0
    x=x-1
    y=y-1
    grid[x][y] = playerNum
    return

def moveBR(x,y, playerNum):
    if x == 7 or y == 7:
        print("invalid move")
        return 0
    grid[x][y] = 0
    x=x+1
    y=y+1
    grid[x][y] = playerNum
    return

def moveBL(x,y, playerNum):
    if x == 7 or y == 0:
        print("invalid move")
        return 0
    grid[x][y] = 0
    x=x+1
    y=y-1
    grid[x][y] = playerNum
    return
