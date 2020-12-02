import sys
counta = 0
countb = 0
for line in sys.stdin.readlines():
    sp = line.split(" ")
    letter = sp[1][0]
    passw = sp[-1]
    bound = [int(x) for x in sp[0].split("-")]
    if passw.count(letter) >= bound[0] and passw.count(letter) <= bound[1]:
        counta += 1
    occ = 0
    if passw[bound[0]-1] == letter:
        occ += 1
    if passw[bound[1]-1] == letter:
        occ += 1
    if occ == 1:
        countb += 1
print(counta)
print(countb)