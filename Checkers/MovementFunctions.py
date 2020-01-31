import os

#Future Ideas:
# Make proper grid GUI

def makeMove(player):
    print("1: Fwd-Right || 2: Fwd-Left  || 3: Jump Fwd-Right || 4: Jump Fwd-Left \n5: Back-Right || 6: Back-Left || 7: Jump Back-Right || 8: Jump Back-Left\n")

    choice = int(input("Move: "))
    print("Which Piece Do You Want To Move?")
    x = int(input("Row: ")) - 1
    y = int(input("Column: ")) - 1

    if x > 7 or x < 0 or y > 7 or y < 0 or grid[x][y] != player.symbol:
        print("Error: Pick a Valid Box\n")
        makeMove(player)
    elif choice == 1:
        if moveFR(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 2:
        if moveFL(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 3:
        if moveJFR(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 4:
        if moveJFL(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 5:
        if moveBR(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 6:
        if moveBL(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 7:
        if moveJBR(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice == 8:
        if moveJBL(x,y,player) == 0:
            print("Error: Make Another Move\n")
            makeMove(player)
    elif choice > 8 or choice < 1:
        print("Error: Select Valid Move\n")
        makeMove(player)
    return

def moveFR(x,y, player):
    if x == 0 or y == 7:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x-1][y+1] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    x=x-1
    y=y+1
    grid[x][y] = player.symbol
    return 1

def moveFL(x,y, player):
    if x == 0 or y == 0:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x-1][y-1] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    x=x-1
    y=y-1
    grid[x][y] = player.symbol
    return 1

def moveBR(x,y, player):
    if x == 7 or y == 7:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x+1][y+1] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    x=x+1
    y=y+1
    grid[x][y] = player.symbol
    return 1

def moveBL(x,y, player):
    if x == 7 or y == 0:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x+1][y-1] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    x=x+1
    y=y-1
    grid[x][y] = player.symbol
    return 1

def moveJFR(x,y, player):
    if x < 2 or y > 5:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x-1][y+1] == empty.symbol or grid[x-1][y+1] == player.symbol or grid[x-2][y+2] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    grid[x-1][y+1] = empty.symbol
    grid[x-2][y+2] = player.symbol

    if player.num == 1:
        p2.pieces = p2.pieces - 1
    elif player.num == 2:
        p1.pieces = p1.pieces - 1
    return 1

def moveJFL(x,y, player):
    if x < 2 or y < 2:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x-1][y-1] == empty.symbol or grid[x-1][y-1] == player.symbol or grid[x-2][y-2] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    grid[x-1][y-1] = empty.symbol
    grid[x-2][y-2] = player.symbol

    if player.num == 1:
        p2.pieces = p2.pieces - 1
    elif player.num == 2:
        p1.pieces = p1.pieces - 1
    return 1

def moveJBR(x,y, player):
    if x > 5 or y > 5:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x+1][y+1] == empty.symbol or grid[x+1][y+1] == player.symbol or grid[x+2][y+2] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    grid[x+1][y+1] = empty.symbol
    grid[x+2][y+2] = player.symbol

    if player.num == 1:
        p2.pieces = p2.pieces - 1
    elif player.num == 2:
        p1.pieces = p1.pieces - 1
    return 1

def moveJBL(x,y, player):
    if x > 5 or y < 2:
        print("Invalid Move: Please Try Again")
        return 0
    if grid[x+1][y-1] == empty.symbol or grid[x+1][y-1] == player.symbol or grid[x+2][y-2] != empty.symbol:
        print("Invalid Move: Please Try Again")
        return 0
    grid[x][y] = empty.symbol
    grid[x+1][y-1] = empty.symbol
    grid[x+2][y-2] = player.symbol

    if player.num == 1:
        p2.pieces = p2.pieces - 1
    elif player.num == 2:
        p1.pieces = p1.pieces - 1
    return 1

def printBoard():
    print("   1   2   3   4   5   6   7   8\n")
    for r in range(8):
        print(r+1, end="  ")
        for c in range(8):
            print(grid[r][c], end="   ")
        print("\n")

#Player Class Inititalization
class Player:
  def __init__(self, pieces, symbol, num):
    self.pieces = pieces
    self.symbol = symbol
    self.num = num
p1 = Player(12, 'X', 1)
p2 = Player(12, 'O', 2)
empty = Player(0, '_', 0)

# Grid Initialization
grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(empty.symbol)

# Board Piece Initialization
grid[0][1],grid[0][3],grid[0][5],grid[0][7],grid[1][0],grid[1][2],grid[1][4],grid[1][6],grid[2][1],grid[2][3],grid[2][5],grid[2][7] = p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol,p1.symbol
grid[5][0],grid[5][2],grid[5][4],grid[5][6],grid[6][1],grid[6][3],grid[6][5],grid[6][7],grid[7][0],grid[7][2],grid[7][4],grid[7][6] = p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol,p2.symbol

#Main Loop
playerTurn = 1
while(p1.pieces > 0 or p2.pieces > 0):
    os.system('cls')
    print("____Checkers____\n\n")
    print(f"Player {playerTurn} Turn\n")
    printBoard()

    if playerTurn == 1:
        makeMove(p1)
        playerTurn = 2
    elif playerTurn == 2:
        makeMove(p2)
        playerTurn = 1

if p1.pieces == 0:
    print("Player 2 Wins!")
elif p2.pieces == 0:
    print("Player 1 Wins!")

input()
input()
