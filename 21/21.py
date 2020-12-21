import sys, re

ingredients = []
allergens = []
aller = set()
foods = set()
for line in sys.stdin.readlines():
    if line and line != "\n":
        m = re.match(r"((?:\w+ )+)\(contains (.+)\)", line)
        ingr = set(m.group(1).strip().split())
        ingredients.append(ingr)
        alle = set(m.group(2).split(", "))
        allergens.append(alle)
        for allergen in alle:
            aller.add(allergen)
        for food in ingr:
            foods.add(food)

possibles = {}
uni = set()
for al in aller:
    possible = set(foods)
    for i in range(len(ingredients)):
        if al in allergens[i]:
            possible &= ingredients[i]
    possibles[al] = possible
    for p in possible:
        uni.add(p)

count = 0
for i in range(len(ingredients)):
    for ingredient in ingredients[i]:
        if ingredient not in uni:
            count += 1
print(count)
