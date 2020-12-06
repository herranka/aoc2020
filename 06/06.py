import sys
qq = []
count = 0
for inp in [x.strip() for x in sys.stdin.read().split("\n\n")]:
    qq.append(inp)
    questions = [x for x in list(inp) if x != "\n"]
    count += len(set(questions))
print(count)

count = 0
for inp in qq:
    n = len(inp.split("\n"))
    answers = [x for x in list(inp) if x != "\n"]
    freq = {}
    for a in answers:
        if a in freq: freq[a] += 1
        else: freq[a] = 1
    c = sum([1 for x in freq.values() if x == n])
    count += c
print(count)