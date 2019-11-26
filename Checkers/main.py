width = int(8)
height = int(8)
grid = []
row = []
bak = "."

for i in range (width):
    row.append(bak)

for i in range (height):
    grid.append(row)

for i in range (len(grid)):
    print(grid[i])


