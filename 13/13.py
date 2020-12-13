import sys
import math
from itertools import chain

# part 1

earliest = int(input())
pre = [(int(x),i) for i,x in enumerate(input().split(",")) if x!= "x"]
shuttles = [x[0] for x in pre]

minv = 10000000
minm = 10000000

for v in shuttles:
    m = ((earliest // v + 1)*v) - earliest
    if m < minm:
        minm = m
        minv = v

print(minv*minm)

# part 2

def prod(*nums):
    p = 1
    for num in nums:
        p *= num
    return p

#cheeky copy-paste
def eu(a: int, b: int):
    if b == 0:
        return (1, 0)
    (x, y) = eu(b, a % b)
    k = a // b
    return (y, x - k * y)

#cheeky copy-paste
def invert_modulo(a: int, n: int) -> int:
    (b, x) = eu(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


def crtn(nums):
    rs = [tup[0] for tup in nums]
    ns = [tup[1] for tup in nums]
    N = prod(*ns)
    ys = [N//n for n in ns]
    zs = [invert_modulo(ys[i], ns[i]) for i in range(len(ns))]
    x = sum([rs[i]*ys[i]*zs[i] for i in range(len(ns))])
    return int(x%N)

"""
# cred till Erik
def crtn(eq):
	p, res = 1, 0
	for rem, md in eq:
		p *= md
	for rem, md in eq:
		pp = p // md
		res = (res + rem * eu(pp, md)[0] * pp) % p
	return res
"""

prepre = [[(tup[0]-tup[1]), tup[0]] for tup in pre]
x = crtn(prepre)
print(x)
