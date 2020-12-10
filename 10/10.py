import sys
lines = []
for line in [int(x.strip()) for x in sys.stdin.readlines()]:
    lines.append(line)

# part 1
ones = 0
threes = 0
origin = max(lines) + 3
sl = sorted(lines)
sl.append(origin)
sl = sl[::-1]
sl.append(0)
for i in range(len(sl)-1):
    if sl[i] - sl[i+1] == 1:
        ones += 1
    elif sl[i] - sl[i+1] == 3:
        threes += 1
print(threes*ones)

# part 2

def fib3(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return fib3(n-1) + fib3(n-2) + fib3(n-3)

origin = max(lines) + 3
sl = sorted(lines)
sl.append(origin)
sl = sl[::-1]
sl.append(0)
steps = [-1 for i in range(len(sl)-1)]
for i in range(len(sl)-1):
    steps[i] = sl[i] - sl[i+1]
ones = [len(y) for y in ''.join([str(x) for x in steps]).split("3") if y]
prod = 1
for one in ones:
    prod *= fib3(one)
print(prod)