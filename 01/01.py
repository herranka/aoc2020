import sys
li = [int(line) for line in sys.stdin.readlines()]

for i in range(len(li)):
    for j in range(i,len(li)):
        if li[i] + li[j] == 2020:
            print(li[i]*li[j])

for i in range(len(li)):
    for j in range(i,len(li)):
        for k in range(j, len(li)):
            if li[i] + li[j] + li[k] == 2020:
                print(li[i]*li[j]*li[k])