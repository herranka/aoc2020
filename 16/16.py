import sys, re
from collections import deque

inp = sys.stdin.read().split("\n\n")

rules = []
fields = []
for line in inp[0].split("\n"):
    m = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", line.strip())
    fields.append(m.group(1))
    r1 = int(m.group(2))
    r2 = int(m.group(3))
    r3 = int(m.group(4))
    r4 = int(m.group(5))
    rules.append((range(r1, r2+1), range(r3, r4+1)))
myticket = [int(x) for x in inp[1].split("\n")[1].split(",")]
tickets = []

for line in inp[2].split("\n")[1:]:
    tickets.append([int(x) for x in line.split(",")])

def valid(num, rule):
    return num in rule[0] or num in rule[1]

def completely_invalid(num, rules):
    some = False
    for j in range(len(rules)):
        if valid(num, rules[j]):
            return False
    return True

count = 0
for ticket in tickets:
    for i,num in enumerate(ticket):
        if completely_invalid(num, rules):
            count += num
print(count)

# part 2

tickets = [ticket for ticket in tickets if not any(map(lambda x: completely_invalid(x, rules), ticket))]

edges = [[False for c in range(2*len(rules)+2)] for r in range(2*len(rules)+2)]
for i in range(1, len(rules)+1):
    edges[0][i] = True
for i in range(len(rules)+1,2*len(rules)+1):
    edges[i][-1] = True

for r, rule in enumerate(rules):
    for i in range(len(rules)):
        if all(valid(tickets[x][i], rule) for x in range(len(tickets))):
            # add edge from rule to ticket i
            edges[r+1][len(edges)//2+i] = True

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

while (p := find_path(edges)):
    for i in range(len(p)-1):
        edges[p[i]][p[i+1]] = False
        edges[p[i+1]][p[i]] = True

mapping = {}
for i,e in enumerate(range(len(edges)//2, len(edges)-1)):
    r = edges[e].index(True) - 1
    mapping[r] = i

dep = []
for i,line in enumerate(inp[0].split("\n")):
    if line.startswith("departure"):
        dep.append(i)

prod = 1
for d in dep:
    i = mapping[d]
    prod *= myticket[i]
print(prod)