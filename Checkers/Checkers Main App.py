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

for r in range(8):
    for c in range(8):
        print(grid[r][c], end="")
    print("\n")
