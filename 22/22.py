import sys
from collections import deque
from copy import copy

data = sys.stdin.read().split("\n\n")
pl1 = [int(x) for x in data[0].strip().split("\n")[1:]]
pl2 = [int(x) for x in data[1].strip().split("\n")[1:]]

# part 1
def count(player):
    c = 0
    for i,e in enumerate(range(len(player))[::-1]):
        c += player[i]*(e+1)
    return c

player1 = deque(pl1)
player2 = deque(pl2)
while len(player1) and len(player2):
    #print(player1, player2)
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

# part 2
def play(player1, player2):
    #print("-------New Game---------")
    history1 = []
    history2 = []
    while len(player1) and len(player2):
        if player1 in history1 or player2 in history2: # p1 wins game
            return True
        history1.append(copy(player1))
        history2.append(copy(player2))
        #print(player1, player2)
        p1 = player1.popleft()
        p2 = player2.popleft()
        if len(player1) >= p1 and len(player2) >= p2:
            # play subgame
            p1sub = deque(list(player1)[:p1])
            p2sub = deque(list(player2)[:p2])
            p1won = play(p1sub, p2sub)
            if len(p1sub) or p1won:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        else:
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)

player1 = deque(pl1)
player2 = deque(pl2)
play(player1, player2)
print(max(count(player1), count(player2)))