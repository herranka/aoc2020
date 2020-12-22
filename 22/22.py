import sys
from collections import deque

data = sys.stdin.read().split("\n\n")
player1 = deque([int(x) for x in data[0].strip().split("\n")[1:]])
player2 = deque([int(x) for x in data[1].strip().split("\n")[1:]])

def count(player):
    c = 0
    for i,e in enumerate(range(len(player))[::-1]):
        c += player[i]*(e+1)
    return c

while len(player1) and len(player2):
    print(player1, player2)
    p1 = player1.popleft()
    p2 = player2.popleft()
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

if len(player1):
    print(count(player1))
else:
    print(count(player2))