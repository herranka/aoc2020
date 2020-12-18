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

def ev2(st): # no parantheses guaranteed
    f = True
    while f:
        off = 0
        f = False
        for m in re.finditer(r"\*(\d+\+\d+(\+\d+)*)", st):
            r = "(" + m.group(1) + ")"
            st = st[:m.start(1)+off] + r + st[m.end(1)+off:]
            off += 2
            f = True
            break
    f = True
    while f:
        off = 0
        f = False
        for m in re.finditer(r"(\d+\+\d+(\+\d+)*)\*", st):
            r = "(" + m.group(1) + ")"
            st = st[:m.start(1)+off] + r + st[m.end(1)+off:]
            off += 2
            f = True
            break
    return eval(st)

count = 0
for line in lines:
    found = True
    while found:
        offset = 0
        found = False
        for m in re.finditer(r"\([\d*+{}]*\)", line):
            query = line[m.start()+1+offset:m.end()-1+offset]
            if not query:continue
            res = str(ev2(query))
            line = line[:m.start()+offset] + res + line[m.end()+offset:]
            offset += len(res)-(m.end()-m.start())
            found = True
    count += eval(str(ev2(line)))
print(count)
