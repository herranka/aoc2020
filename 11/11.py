import sys
from copy import copy, deepcopy
lines = []
for line in sys.stdin.readlines():
    lines.append(line)

p1 = [list(x.strip()) for x in lines[::]]
# part 1

def inbounds(li,r,c):
    return (r >= 0 and c >= 0 and r < len(li) and c < len(li[0]))

def occ(li, r, c):
    count = 0
    neigh = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for n in neigh:
        if inbounds(li, r+n[0], c+n[1]) and li[r+n[0]][c+n[1]] == "#":
            count += 1
    return count

def count_occ(li):
    count = 0
    for line in li:
        count += line.count("#")
    return count

def print_li(li):
    for line in li:
        print(''.join(line))
    print("--------------------------")

#print_li(p1)
changed = True
while changed:
    ori = deepcopy(p1)
    changed = False
    for r, line in enumerate(ori):
        for c, ch in enumerate(line):
            if ori[r][c] != ".":
                o = occ(ori, r, c)
                if ch == "#" and o >= 4:
                    p1[r][c] = "L"
                    changed = True
                elif ch == "L" and o == 0:
                    p1[r][c] = "#"
                    changed = True
    #print_li(p1)
print(count_occ(p1))

# part 2
def occ2(li, r, c):
    count = 0
    neigh = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for n in neigh:
        offset = 1
        while inbounds(li, r+n[0]*offset, c+n[1]*offset) and li[r+n[0]*offset][c+n[1]*offset] == ".":
            offset += 1
        if inbounds(li, r+n[0]*offset, c+n[1]*offset) and li[r+n[0]*offset][c+n[1]*offset] == "#":
            count += 1
    return count

p2 = [list(x.strip()) for x in lines[::]]
#print_li(p2)
changed = True
while changed:
    ori = deepcopy(p2)
    changed = False
    for r, line in enumerate(ori):
        for c, ch in enumerate(line):
            if ori[r][c] != ".":
                o = occ2(ori, r, c)
                if ch == "#" and o >= 5:
                    p2[r][c] = "L"
                    changed = True
                elif ch == "L" and o == 0:
                    p2[r][c] = "#"
                    changed = True
    #print_li(p2)
print(count_occ(p2))