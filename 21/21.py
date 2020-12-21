import sys, re
from collections import deque

ingredients = []
allergens = []
aller = set()
foods = set()
for line in sys.stdin.readlines():
    if line and line != "\n":
        m = re.match(r"((?:\w+ )+)\(contains (.+)\)", line)
        ingr = set(m.group(1).strip().split())
        ingredients.append(ingr)
        alle = set(m.group(2).split(", "))
        allergens.append(alle)
        for allergen in alle:
            aller.add(allergen)
        for food in ingr:
            foods.add(food)

possibles = {}
uni = set()
for al in aller:
    possible = set(foods)
    for i in range(len(ingredients)):
        if al in allergens[i]:
            possible &= ingredients[i]
    possibles[al] = possible
    for p in possible:
        uni.add(p)

count = 0
for i in range(len(ingredients)):
    for ingredient in ingredients[i]:
        if ingredient not in uni:
            count += 1
print(count)

# part 2

def find_path(edges):
    visited = [False for i in range(len(edges))]
    pred = [None for i in range(len(edges))]
    q = deque([0])
    visited[0] = True
    while len(q) !=0:
        cur = q.popleft()
        if cur == len(edges)-1: # found drain
            break
        neigh = (i for i in range(len(edges)) if edges[cur][i] and not visited[i])
        for n in neigh:
            visited[n] = True
            pred[n] = cur
            q.append(n)
    path = []
    if cur == len(edges)-1: # found drain
        while cur:
            path.append(cur)
            cur = pred[cur]
        path.append(0)
        path = path[::-1]
    return path

edges = [[False for c in range(2*len(aller)+2)] for r in range(2*len(aller)+2)]
for i in range(1, len(aller)+1):
    edges[0][i] = True
for i in range(len(aller)+1,2*len(aller)+1):
    edges[i][-1] = True

print(edges)

allerlist = sorted(list(aller))
foodlist = sorted(list(uni))
print(foodlist)
for a in allerlist:
    print(possibles[a])
for i,key in enumerate(allerlist):
    for ingredient in possibles[key]:
        j = foodlist.index(ingredient)
        edges[i+1][len(edges)//2+j] = True

print(edges)

while (p := find_path(edges)):
    for i in range(len(p)-1):
        edges[p[i]][p[i+1]] = False
        edges[p[i+1]][p[i]] = True

mapping = {}
for i,e in enumerate(range(len(edges)//2, len(edges)-1)):
    r = edges[e].index(True) - 1
    mapping[allerlist[r]] = foodlist[i]
out = []
for al in allerlist:
    out.append(mapping[al])
print(','.join(out))