import sys

N = 25
lines = [int(line.strip()) for line in sys.stdin.readlines()]

def anysum(li,val):
    for v1 in range(len(li)):
        for v2 in range(v1+1, len(li)):
            s = li[v1] + li[v2]
            if s == val:
                return True
    return False

for i,line in enumerate(lines):
    if i < N:
        continue
    anys = anysum(lines[i-N:i], line)
    if not anys:
        print(line)
        n = line
        break

# part 2
numcon = 2
while numcon < len(lines):
    for i in range(numcon-1, len(lines)):
        s = sum(lines[i-numcon+1:numcon+1])
        if s == n:
            nums = lines[i-numcon+1:numcon+1]
            nums.sort()
            print(nums[0] + nums[-1])
            sys.exit()
    numcon += 1
    

