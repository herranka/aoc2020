from copy import deepcopy

C = 30
R = 30
H = 30
matrix = [[[False for i in range(C)] for j in range(R)] for k in range(H)]

import sys

count = 0
inp = []

for r,line in enumerate(sys.stdin.readlines()):
    line = line.strip()
    inp.append(line)
    for c,ch in enumerate(line):
        if ch=="#":
            matrix[H//2][R//2 + r][C//2 + c] = True
            count += 1

def inbounds(h, r, c):
    return h < H and h >= 0 \
       and r < R and r >= 0 \
       and c < C and c >= 0
    

def neigh(matrix, h, r, c):
    ret = 0
    for h1 in range(h-1, h+2):
        for r1 in range(r-1, r+2):
            for c1 in range(c-1, c+2):
                if inbounds(h1, r1, c1) and matrix[h1][r1][c1]:
                    ret += 1
    return (ret-1) if matrix[h][r][c] else ret


def sim(matrix):
    ret = 0
    tempm = deepcopy(matrix)
    for h in range(H):
        for r in range(R):
            for c in range(C):
                n = neigh(tempm, h, r, c)
                if tempm[h][r][c]:
                    if not (n == 2 or n == 3):
                        matrix[h][r][c] = False
                        ret -= 1
                else:
                    if n == 3:
                        matrix[h][r][c] = True
                        ret += 1
    return ret
"""
def printm(matrix):
    print("----------------------")
    for h in range(H//2-4, H//2+11):
        something = False
        lines = []
        for r in range(R//2-4, R//2+11):
            line = []
            for c in range(C//2-4, C//2+11):
                if matrix[h][r][c]:
                    something = True
                    line.append("#")
                else:
                    line.append(".")
            line = ''.join(line)
            lines.append(line)
        if something:
            for line in lines:
                print(line)
            print("")
"""
for i in range(6):
    count += sim(matrix)
print(count)

# part 2

K = 30
H = 30
R = 30
C = 30

def inbounds(k, h, r, c):
    return k < K and k >= 0 \
       and h < H and h >= 0 \
       and r < R and r >= 0 \
       and c < C and c >= 0
    

def neigh(matrix, k, h, r, c):
    ret = 0
    for k1 in range(k-1, k+2):
        for h1 in range(h-1, h+2):
            for r1 in range(r-1, r+2):
                for c1 in range(c-1, c+2):
                    if inbounds(k1, h1, r1, c1) and matrix[k1][h1][r1][c1]:
                        ret += 1
    return (ret-1) if matrix[k][h][r][c] else ret


def sim(matrix):
    ret = 0
    tempm = deepcopy(matrix)
    for k in range(K):
        for h in range(H):
            for r in range(R):
                for c in range(C):
                    n = neigh(tempm, k, h, r, c)
                    if tempm[k][h][r][c]:
                        if not (n == 2 or n == 3):
                            matrix[k][h][r][c] = False
                            ret -= 1
                    else:
                        if n == 3:
                            matrix[k][h][r][c] = True
                            ret += 1
    return ret

matrix = [[[[False for i in range(C)] for j in range(R)] for l in range(H)] for s in range(K)]
count = 0
for r,line in enumerate(inp):
    for c,ch in enumerate(line):
        if ch=="#":
            matrix[K//2][H//2][R//2 + r][C//2 + c] = True
            count += 1
for i in range(6):
    count += sim(matrix)
print(count)
