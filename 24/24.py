import sys

instructions = [x.strip() for x in sys.stdin.readlines()]

directions = {"ne", "nw", "se", "sw", "w", "e"}

def move(x,y,st):
    if st == "w":
        return  [x-1, y]
    elif st == "e":
        return [x+1, y]
    elif st == "nw":
        return [x, y-1]
    elif st == "ne":
        return [x+1,y-1]
    elif st == "sw":
        return [x-1, y+1]
    elif st == "se":
        return [x, y+1]

def flip(grid, x, y):
    grid[x][y] = not grid[x][y]

grid = [[False for i in range(100)] for j in range(100)]
origin = [50,50]

for line in instructions:
    i = 0
    x,y = origin
    while i < len(line):
        if line[i:i+2] in directions:
            x,y = move(x,y,line[i:i+2])
            i += 2
        else:
            x,y = move(x,y, line[i])
            i += 1
    flip(grid, x, y)

count = 0
for line in grid:
    count += line.count(True)
print(count)
