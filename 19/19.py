import sys, re
import regex

sections = [x.split("\n") for x in sys.stdin.read().split("\n\n") if x]
for i in range(len(sections)):
    sections[i] = [x.strip() for x in sections[i] if x]
sections[0] = [x.split(" ") for x in sections[0]]

def parse_rule(i, prerules, rules):
    rule = prerules[i][::]
    for j,part in enumerate(rule):
        if part.isnumeric():
            num = int(part)
            if num in rules:
                rule[j] = rules[num]
            else:
                rule[j] = parse_rule(num, prerules, rules)
        elif part.startswith("\"") and part.endswith("\""):
            rule[j] = part[1:-1]
    st = "(?:" + ''.join(rule) + ")"
    rules[i] = st
    return st

def parse_all(prerules):
    rules = {}
    for i in prerules:
        parse_rule(i, prerules, rules)
    return rules

def count_matching(rules, strings):
    count = 0
    zero = re.compile("^" + rules[0] + "$")
    for line in strings:
        line = line.strip()
        if (m:=zero.match(line)):
            count += 1
    return count

prerules = {}
for rule in sections[0]:
    col = rule[0].find(":")
    i = int(rule[0][:col])
    rule = rule[1:]
    prerules[i] = rule

rules = parse_all(prerules)
print(count_matching(rules, sections[1]))

# part 2

def join(li, st):
    res = []
    for rule in li:
        for part in rule:
            res.append(part)
        res.append(st)
    return res[:-1]

prerules[8] = ["42", "+"]
eleven = []
for i in range(4):
    eleven.append(["(?:", "42", "(?:", "42", "){%d}"%i, "(?:", "31", "){%d}"%i, "31", ")"])
prerules[11] = join(eleven, "|")

rules = parse_all(prerules)
print(count_matching(rules,sections[1]))