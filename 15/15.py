starting = [int(x) for x in input().split(",")]

def update(m,num,i):
    if num in m:
        j,k = m[num]
        m[num] = [k,i]
    else:
        m[num] = [None,i]

def diff(m,num):
    if m[num][0] == None:
        return m[num][1]
    return m[num][1]-m[num][0]

def find_nth(n):
    m = {}
    for i in range(len(starting)):
        m[starting[i]] = [None,i]

    i = len(starting)
    num = starting[i-1]
    while i < n:
        #update num
        if num in m:
            if m[num][0] == None:
                num = 0
            else:
                num = diff(m,num)
        else:
            num = 0
        #update m
        update(m,num,i)
        i += 1
    return num

# part 1
print(find_nth(2020))
# part 2
print(find_nth(30000000))