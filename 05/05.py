from sys import stdin

def mid(a,b):
    return (a+b)//2

def sid(row, col):
    return row*8 + col

def search(st, slo, shi):
    nrows = 2**len(st)
    lo = 0
    hi = nrows-1
    #print(st, lo, hi, slo, shi)
    for i,ch in enumerate(st):
        m = mid(lo,hi)
        if ch == slo:
            hi = m
        elif ch == shi:
            lo = m
    return hi

lines = []
lowest = 127
highest = 0
for line in (x.strip() for x in stdin.readlines()):
    lines.append(line)
    row = search(line[:7], "F", "B")
    col = search(line[7:], "L", "R")
    si = sid(row,col)
    if si < lowest:
        lowest = si
    if si > highest:
        highest = si
    #print(row, col, si)
print(highest)

# part 2

visited = [None for i in range(2**10+1)]

for line in lines:
    row = search(line[:7], "F", "B")
    col = search(line[7:], "L", "R")
    si = sid(row,col)
    visited[si] = (row,col)
    

subli = visited[lowest:highest+1]
for i, si in enumerate(subli):
    if si == None:
        left = subli[i-1] if i != 0 else None
        right = subli[i+1] if i+1 != len(subli) else None
        if left != None and right != None:
            # found
            print((sid(*left)+sid(*right))//2)
            break
