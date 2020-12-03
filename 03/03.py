from functools import reduce
import sys

map = []
for line in sys.stdin.readlines(): #includes newline
    map.append(line.strip())

count = 0
x = 0
y = 0
while x < len(map[0]) and y < len(map):
    if (map[y][x]) == "#":
        count += 1
    x += 3
    x %= (len(map[0]))
    y += 1
print(count)

prods = []
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
for sl in slopes:
    x = 0
    y = 0
    count = 0
    while x < len(map[0]) and y < len(map):
        if (map[y][x]) == "#":
            count += 1
        x += sl[0]
        x %= (len(map[0]))
        y += sl[1]
    prods.append(count)
product = reduce(lambda x,y: x*y, prods)
print(product)