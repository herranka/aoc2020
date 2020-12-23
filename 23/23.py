inp = [int(x) for x in input()]
n = len(inp)

li = inp[::]
current = 0
t = 0
while t < 100:
    t += 1
    curval = li[current]
    three = [li[i%n] for i in range(current+1,current+4)]
    li = [num for num in li if num not in three]
    ta = (curval-2) % n + 1
    while ta not in li:
        ta = (ta - 2) % n + 1
    target = li.index(ta)
    last = target
    for i in range(3):
        last = (last + 1) % len(li)
        li.insert(last, three[i])
    current = (li.index(curval) + 1) % n

one = li.index(1)
print(''.join(str(x) for x in (li[one+1:] + li[:one])))
