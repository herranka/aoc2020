import sys
lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

def apply_mask(val, mask):
    binary = format(val, '036b')
    out = []
    for i in range(len(mask)):
        if mask[i] == "1":
            out.append("1")
        elif mask[i] == "0":
            out.append("0")
        else:
            out.append(binary[i])
    return int(''.join(out), 2)

def store(val, addr, mask, mem):
    mem[addr] = apply_mask(val,mask)

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
mem = [0 for i in range(100000)]
for line in lines:
    var, val = line.split(" = ")
    if var == "mask":
        mask = val
    else:
        address = int(var[4:-1])
        val = int(val)
        store(val, address, mask, mem)
print(sum([x for x in mem]))

# part 2

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

bin = "{:06b}"

floating = (1<<36)-1
fixed = (1<<36)-1
mem = {}
for line in lines:
    var, val = line.split(" = ")
    if var == "mask":
        floating, fixed = masks(val)
        #print("-------------------")
        #print("masks: ", bin.format(floating),"\n"," "*6, bin.format(fixed))
    else:
        address = int(var[4:-1])
        val = int(val)
        for subset in subsets(floating):
            #print("subset:",bin.format(subset))
            #print("fixed: ", bin.format(fixed))
            #print("oldadd:", bin.format(address), ":", address)
            newaddr = subset | (~floating & (fixed | address))
            #print("addres:", bin.format(newaddr), ":", newaddr)
            mem[newaddr] = val
print(sum([num for num in mem.values()]))