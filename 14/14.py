import sys
lines = [line.strip() for line in sys.stdin.readlines()]

def masks(st):
    fl = 0
    fi = 0
    for i,ch in enumerate(st):
        if ch == "1":
            fi += 1<<(len(st)-i-1)
        elif ch == "X":
            fl += 1<<(len(st)-i-1)
    return fl, fi

floating = 0
fixed = 0
mem = [0 for i in range(100000)]
for line in lines:
    var, val = line.split(" = ")
    if var == "mask":
        floating, fixed = masks(val)
    else:
        address = int(var[4:-1])
        val = int(val)
        mem[address] = (fixed & ~floating) | (floating & val)
print(sum(mem))

# part 2

def subsets(mask):
    subset = mask
    while subset:
        yield subset
        subset = mask & (subset-1)
    yield subset

floating = (1<<36)-1
fixed = (1<<36)-1
mem = {}
for line in lines:
    var, val = line.split(" = ")
    if var == "mask":
        floating, fixed = masks(val)
    else:
        address = int(var[4:-1])
        val = int(val)
        for subset in subsets(floating):
            newaddr = subset | (~floating & (fixed | address))
            mem[newaddr] = val
print(sum(mem.values()))