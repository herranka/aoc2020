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

def flip(black, x, y):
    if (x,y) in black:
        black.remove((x,y))
    else:
        black.add((x,y))

origin = [50,50]
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