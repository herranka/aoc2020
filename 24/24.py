import sys
from copy import copy

instructions = [x.strip() for x in sys.stdin.readlines()]

directions = {"ne", "nw", "se", "sw", "w", "e"}

def move(x,y,st):
    if st == "w":
        return  (x-1, y)
    elif st == "e":
        return (x+1, y)
    elif st == "nw":
        return (x, y-1)
    elif st == "ne":
        return (x+1,y-1)
    elif st == "sw":
        return (x-1, y+1)
    elif st == "se":
        return (x, y+1)

def flip(bl, x, y):
    if (x,y) in bl:
        bl.remove((x,y))
    else:
        bl.add((x,y))

origin = (50,50)
black = set()

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
    flip(black, x, y)

print(len(black))

# part 2

def neighbours(x, y):
    return (move(x,y,m) for m in directions)

def black_neigh(bl, x,y):
    return sum(1 for pos in neighbours(x,y) if pos in bl)

day = 1
while day <= 100:
    blcopy = copy(black)
    for x,y in blcopy:
        count = black_neigh(blcopy, x, y)
        if count == 0 or count > 2:
            black.remove((x,y))
        for nx,ny in neighbours(x,y):
            ncount = black_neigh(blcopy, nx, ny)
            if ncount == 2:
                black.add((nx,ny))
    day += 1
print(len(black))