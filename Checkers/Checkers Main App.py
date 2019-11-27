#Functions

def makeMove(playerNum):
    print("Enter 1: FR // 2: FL // 3: BR // 4: BL \n5: JFR // 6: JFL // 7: JBR // 8: JBL\n")
    choice = int(input())
    print("Which piece do you want to move?")
    x = int(input("row: "))
    y = int(input("column: "))
    x = x - 1
    y = y - 1

    if choice == 1:
        if moveFR(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 2:
        if moveFL(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 3:
        if moveBR(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 4:
        if moveBL(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 5:
        if moveJFR(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 6:
        if moveJFL(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 7:
        if moveJBR(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    elif choice == 8:
        if moveJBL(x,y,playerNum) == 0:
            print("Error: Make Another Move\n")
            makeMove(playerNum)
    return

def moveFR(x,y, playerNum):
    if x == 0 or y == 7:
        print("invalid move1")
        return 0
    if grid[x-1][y+1] != 0:
        print("invalid move2")
        return 0
    grid[x][y] = 0
    x=x-1
    y=y+1
    grid[x][y] = playerNum
    return 1

def moveFL(x,y, playerNum):
    if x == 0 or y == 0:
        print("invalid move")
        return 0
    if grid[x-1][y-1] != 0:
        print("invalid move2")
        return 0
    grid[x][y] = 0
    x=x-1
    y=y-1
    grid[x][y] = playerNum
    return 1

def moveBR(x,y, playerNum):
    if x == 7 or y == 7:
        print("invalid move")
        return 0
    if grid[x+1][y+1] != 0:
        print("invalid move2")
        return 0
    grid[x][y] = 0
    x=x+1
    y=y+1
    grid[x][y] = playerNum
    return 1

def moveBL(x,y, playerNum):
    if x == 7 or y == 0:
        print("invalid move")
        return 0
    if grid[x+1][y-1] != 0:
        print("invalid move2")
        return 0
    grid[x][y] = 0
    x=x+1
    y=y-1
    grid[x][y] = playerNum
    return 1

def moveJFR(x,y, playerNum):
    if x < 2 or y > 5:
        print("invalid move")
        return 0
    if grid[x-1][y+1] == 0:
        print("invalid move")
        return 0
    if grid[x-2][y+2] != 0:
        print("invalid move")
        return 0
    grid[x][y] = 0
    grid[x-1][y+1] = 0
    grid[x-2][y+2] = playerNum

    if playerNum == 1:
        player2Pieces = player2Pieces - 1
    elif playerNum == 2:
        player1Pieces = player2Pieces - 1
    return 1

def moveJFL(x,y, playerNum):
    if x < 2 or y < 2:
        print("invalid move")
        return 0
    if grid[x-2][y-2] != 0:
        print("invalid move")
        return 0
    grid[x][y] = 0
    grid[x-1][y-1] = 0
    grid[x-2][y-2] = playerNum

    if playerNum == 1:
        player2Pieces = player2Pieces - 1
    elif playerNum == 2:
        player1Pieces = player2Pieces - 1
    return 1

def moveJBR(x,y, playerNum):
    if x > 5 or y > 5:
        print("invalid move")
        return 0
    if grid[x+2][y+2] != 0:
        print("invalid move")
        return 0
    grid[x][y] = 0
    grid[x+1][y+1] = 0
    grid[x+2][y+2] = playerNum

    if playerNum == 1:
        player2Pieces = player2Pieces - 1
    elif playerNum == 2:
        player1Pieces = player2Pieces - 1
    return 1

def moveJBL(x,y, playerNum):
    if x > 5 or y < 2:
        print("invalid move")
        return 0
    if grid[x+2][y-2] != 0:
        print("invalid move2")
        return 0
    grid[x][y] = 0
    grid[x+1][y-1] = 0
    grid[x+2][y-2] = playerNum

    if playerNum == 1:
        player2Pieces = player2Pieces - 1
    elif playerNum == 2:
        player1Pieces = player1Pieces - 1
    return 1

grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

        
#Player One = 1
grid[0][1] = 1
grid[0][3] = 1
grid[0][5] = 1
grid[0][7] = 1
grid[1][0] = 1
grid[1][2] = 1
grid[1][4] = 1
grid[1][6] = 1
grid[2][1] = 1
grid[2][3] = 1
grid[2][5] = 1
grid[2][7] = 1

#Player Two = 2
grid[5][0] = 2
grid[5][2] = 2
grid[5][4] = 2
grid[5][6] = 2
grid[6][1] = 2
grid[6][3] = 2
grid[6][5] = 2
grid[6][7] = 2
grid[7][0] = 2
grid[7][2] = 2
grid[7][4] = 2
grid[7][6] = 2

print("Before Move\n")
for r in range(8):
    for c in range(8):
        print(grid[r][c], end="")
    print("\n")

error = 0
player1Pieces = 12
player2Pieces = 12


makeMove(2)

print("After Move\n")
for r in range(8):
    for c in range(8):
        print(grid[r][c], end="")
    print("\n")
    





