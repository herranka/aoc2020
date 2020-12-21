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

def subsets(mask):
    subset = mask
    while subset:
        yield subset
        subset = mask & (subset-1)
    yield subset

floating = 0
fixed = 0
mem = {} # part 1
mem2 = {} # part 2
for line in lines:
    var, val = line.split(" = ")
    if var == "mask":
        floating, fixed = masks(val)
    else:
        address = int(var[4:-1])
        val = int(val)
        mem[address] = (fixed & ~floating) | (floating & val)
        for subset in subsets(floating):
            newaddr = subset | (~floating & (fixed | address))
            mem2[newaddr] = val
print(sum(mem.values()))
print(sum(mem2.values()))