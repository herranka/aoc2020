import sys

N = 25
lines = [int(line.strip()) for line in sys.stdin.readlines()]

def anysum(li,val):
    for v1 in range(len(li)):
        for v2 in range(v1+1, len(li)):
            s = li[v1] + li[v2]
            if s == val:
                return True
    return False

for i,line in enumerate(lines):
    if i < N:
        continue
    anys = anysum(lines[i-N:i], line)
    if not anys:
        print(line)
        n = line
        break

# part 2
con = 2
while con < len(lines):
    s = sum(lines[:con])
    for i in range(con, len(lines)):
        s += lines[i]
        s -= lines[i-con]
        if s == n:
            li = lines[i-con+1:i+1]
            li.sort()
            print(li[0]+li[-1])
            sys.exit()
    con += 1
    

