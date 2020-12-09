import sys

acc = 0
i = 0
code = []
ran = set()
for ins,val in [x.split() for x in sys.stdin.readlines()]:
    code.append((ins,val))

while i >= 0 and i < len(code):
    ins = code[i][0]
    val = int(code[i][1])
    if i in ran:
        loop = True
        break
    ran.add(i)
    if ins == "acc":
        acc += val
        i += 1
    elif ins == "jmp":
        i += val
    elif ins == "nop":
        i += 1
print(acc)

def testnop(jmpi):
    restore = code[jmpi]
    code[jmpi] = ("nop", "+0")
    i = 0
    acc = 0
    ran = set()
    while i >= 0 and i < len(code):
        ins = code[i][0]
        val = int(code[i][1])
        if i in ran:
            code[jmpi] = restore
            return False
        ran.add(i)
        if ins == "acc":
            acc += val
            i += 1
        elif ins == "jmp":
            i += val
        elif ins == "nop":
            i += 1
    return acc

jmps = [i for i,tup in enumerate(code) if tup[0]=="jmp"]
for jmp in jmps:
    if acc:=testnop(jmp):
        print(acc)
        break