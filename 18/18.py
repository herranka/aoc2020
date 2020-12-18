import sys
import re

lines = []
for line in sys.stdin.readlines():
    line = line.strip().replace(" ", "")
    lines.append(line)

def is_op(st):
    return st == "*" or st == "+"

def calc(left, right, op):
    ret = 0
    if op == "+":
        ret = left+right
    elif op == "*":
        ret = left*right
    else:
        print("wtf")
    return ret

def encapsuled(line):
    if not line:
        return False
    if line[0] != "(" or line[-1] != ")":
        return False
    p = 1
    i = len(line)-2
    while p > 0 and i >= 0:
        if line[i] == ")":
            p += 1
        elif line[i] == "(":
            p -= 1
        if p == 0:
            break
        i -= 1
    return p == 0 and i == 0

def ev(line):
    if encapsuled(line):
        return ev(line[1:-1])
    i = len(line)-1
    pars = 0
    while i >= 0:
        if is_op(line[i]) and pars == 0:
            left = line[0:i]
            op = line[i]
            right = line[i+1:]
            return calc(ev(left),ev(right),op)
            break
        if line[i] == ")": pars += 1
        elif line[i] == "(": pars -=1
        i-=1
    return int(line)

count = 0
for line in lines:
    count += ev(line)
print(count)


# part 2

def enc(st):
    return "(" + st + ")"

def replace_all(st, regex, rfunc):
    f = True
    while f:
        off = 0
        f = False
        for m in re.finditer(regex, st):
            r = rfunc(m.group(1))
            st = st[:m.start(1)+off] + r + st[m.end(1)+off:]
            off += len(r) - len(m.group(1))
            f = True
    return st

def ev2(st): # no parantheses guaranteed
    st = replace_all(st, r"\*(\d+\+\d+(\+\d+)*)", enc)
    st = replace_all(st, r"(\d+\+\d+(\+\d+)*)\*", enc)
    return eval(st)

count = 0
for line in lines:
    line = replace_all(line, r"(\([\d*+{}]*\))", lambda x: str(ev2(x[1:-1])))
    count += eval(str(ev2(line)))
print(count)
