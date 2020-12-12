import sys
from math import sin, cos, radians

inst = []
for line in sys.stdin.readlines():
    line = line.strip()
    ins = line[0]
    val = int(line[1:])
    inst.append((ins,val))

def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])

dist = [0,0]
angle = 0

for ins,val in inst:
    if ins == "N":
        dist[1] += val
    elif ins == "S":
        dist[1] -= val
    elif ins == "E":
        dist[0] += val
    elif ins == "W":
        dist[0] -= val
    elif ins == "L":
        angle = (angle + val) % 360
    elif ins == "R":
        angle = (angle - val) % 360
    elif ins == "F":
        dist[0] += int(cos(radians(angle))*val)
        dist[1] += int(sin(radians(angle))*val)

print(manhattan(dist))

# part 2

wpos = [10,1] # relative
dist = [0,0] # moved from origin

def mult(pos, val):
    return [pos[0]*val, pos[1]*val]

def add(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]

def left(pos):
    return [-pos[1], pos[0]]

def right(pos):
    return [pos[1], -pos[0]]

#print(wpos, dist)
for ins,val in inst:
    if ins == "N":
        wpos[1] += val
    elif ins == "S":
        wpos[1] -= val
    elif ins == "E":
        wpos[0] += val
    elif ins == "W":
        wpos[0] -= val
    elif ins == "L":
        if val == 180:
            wpos = mult(wpos, -1)
        elif val == 270:
            wpos = right(wpos)
        else:
            wpos = left(wpos)
    elif ins == "R":
        if val == 180:
            wpos = mult(wpos, -1)
        elif val == 270:
            wpos = left(wpos)
        else:
            wpos = right(wpos)
    elif ins == "F":
        di = wpos
        move = mult(di, val)
        dist = add(dist, move)
    #print((ins,val), wpos, dist)

print(manhattan(dist))