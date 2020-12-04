import sys

# part 1
count = 0
data = [x for x in sys.stdin.read().split("\n") if x != "\n"]
req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
found = set()
for dat in data:
    if dat == "":
        got = True
        for r in req:
            if r not in found:
                got = False
                break
        if got: count += 1
        found = set()
        continue
    fields = [y.split(":")[0] for y in dat.split(" ")]
    for field in fields:
        if field in req:
            found.add(field)
print(count)

# part 2
def valid(dat):
    req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if dat[0] not in req:
        return False
    if dat[0] == "byr":
        try:
            num = int(dat[1])
            if num < 1920 or num > 2002:
                return False
        except:
            return False
    elif dat[0] == "iyr":
        try:
            num = int(dat[1])
            if num < 2010 or num > 2020:
                return False
        except:
            return False
    elif dat[0] == "eyr":
        try:
            num = int(dat[1])
            if num < 2020 or num > 2030:
                return False
        except:
            return False
    elif dat[0] == "hgt":
        hgt = dat[1][:-2]
        meas = dat[1][-2:]
        try:
            num = int(hgt)
            if meas == "cm":
                if num < 150 or num > 193:
                    return False
            elif meas == "in":
                if num < 59 or num > 76:
                    return False
            else:
                return False
        except:
            return False
    elif dat[0] == "hcl":
        if dat[1][0] != "#" or len(dat[1]) != 7:
            return False
        hexes = "abcdef0123456789"
        for ch in dat[1][1:]:
            if ch not in hexes:
                return False
    elif dat[0] == "ecl":
        possible = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        if dat[1] not in possible:
            return False
    elif dat[0] == "pid":
        possible = set(list("0123456789"))
        if len(dat[1]) != 9:
            return False
        for ch in dat[1]:
            if ch not in possible:
                return False
    return True
    
count = 0
req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
found = set()
for dat in data:
    if dat == "":
        print(found)
        got = True
        for r in req:
            if r not in found:
                print("not found")
                got = False
                break
        if got: count += 1
        found = set()
        continue
    fields = [y.split(":") for y in dat.split(" ")]
    for field in fields:
        if (valid(field)):
            found.add(field[0])
got = True
for r in req:
    if r not in found:
        print("not found")
        got = False
        break
if got: count += 1

print(count)