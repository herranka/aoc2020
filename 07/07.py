import sys
import re

lines = []
for line in sys.stdin.readlines():
    lines.append(line)

m = {}
for line in lines:
    if "no" in line:
        continue
    origin, rules = line.split(" bags contain ")
    rules = [x.strip().strip(".") for x in rules[:-1].split(", ")]
    for rule in rules:
        if r:=re.match(r"[0-9]+ (\w+ \w+)", rule):
            color = r.group(1)
            if color in m and origin not in m[color]:
                m[color].add(origin)
            else:
                m[color] = set()
                m[color].add(origin)
found = set()
def count(color):
    if not color in m:
        return
    for neigh in m[color]:
        found.add(neigh)
        count(neigh)

count("shiny gold")
print(len(found))

# part 2
mm = {}
for line in lines:
    origin, rules = line.split(" bags contain ")
    rules = [x.strip().strip(".") for x in rules[:-1].split(", ")]
    for rule in rules:
        if r:=re.match(r"([0-9]+) (\w+ \w+)", rule):
            num = int(r.group(1))
            color = r.group(2)
            if not origin in mm: mm[origin] = []
            mm[origin].append((color, num))
def count2(color,num):
    if color not in mm: return 0
    c = 0
    for tup in mm[color]:
        c += count2(*tup) + tup[1]*1
    return c*num

print(count2("shiny gold", 1))