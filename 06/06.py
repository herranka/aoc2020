import sys

groups = []
for group in sys.stdin.read().split("\n\n"):
    answers = [a.strip() for a in group.split("\n")]
    groups.append(answers)

# part 1
print(sum(len(set(''.join(answers))) for answers in groups))

# part 2
count = 0
for answers in groups:
    freq = {}
    for a in ''.join(answers):
        if a in freq: freq[a] += 1
        else: freq[a] = 1
    count += sum(1 for x in freq.values() if x == len(answers))
print(count)
