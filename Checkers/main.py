width = int(8)
height = int(8)
grid = []
row = []
bak = 0

for i in range (width):
    row.append(bak)

for i in range (height):
    grid.append(row)

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
grid[5][0] = 1
grid[5][2] = 1
grid[5][4] = 1
grid[5][6] = 1
grid[6][1] = 1
grid[6][3] = 1
grid[6][5] = 1
grid[6][7] = 1
grid[7][0] = 1
grid[7][2] = 1
grid[7][4] = 1
grid[7][6] = 1

for i in range (len(grid)):
    print(grid[i])
    print("\n")