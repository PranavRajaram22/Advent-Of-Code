from collections import defaultdict
from itertools import batched
from multiprocessing.forkserver import connect_to_new_process

with open('2020 input') as file:
    rules = [rule.strip() for rule in file]

graph = defaultdict(list)


bagswithoutnumsdict = defaultdict(list)
bagswithnumsdict = defaultdict(list)


for rule in rules:
    rule = rule.split(" ")
    while "bagswithoutnums" in rule:
        rule.remove('bagswithoutnums')
    while "contain" in rule:
        rule.remove('contain')
    while "bag" in rule:
        rule.remove('bag')
    while "bag," in rule:
        rule.remove('bag,')
    while "bags." in rule:
        rule.remove('bags.')
    while "bags" in rule:
        rule.remove('bags')
    while "bags," in rule:
        rule.remove('bags,')
    while "bag." in rule:
        rule.remove('bag.')
    container = []
    container.append(rule.pop(0))
    container.append(rule.pop(0))
    container = ' '.join(container)

    for i, element in enumerate(rule):
        try:
            rule[i] = int(element)
        except ValueError:
            pass
    bagswithnums = list(batched(rule, 3))
    for i, bag in enumerate(bagswithnums):
        num, b = bag[0], bag[1:]
        b = " ".join(b)
        bagswithnums[i] = (num, b)

    for b in bagswithnums:
        if b != ('no', 'other'):
            bagswithnumsdict[container].append({b[1]:b[0]})
        else:
            bagswithnumsdict[container] = []
    i = 0
    while i < len(rule):
        if isinstance(rule[i], int):
            rule.pop(i)
        else:
            i += 1

    containedbags = []
    currbag = []

    for i in range(len(rule)):
        if i%2 == 1:
            currbag.append(rule[i])
        else:
            if i != 0:
                containedbags.append(" ".join(currbag))
            currbag = [rule[i]]
    containedbags.append(" ".join(currbag))

    bagswithoutnumsdict[container] = containedbags

for container in bagswithoutnumsdict.keys():
    containedbags = bagswithoutnumsdict[container]
    for bag in containedbags:
        graph[bag].append(container)


bags_in_other_bags = graph.keys()
bags_not_in_other_bags = set()

for bag in bags_in_other_bags:
    for b in graph[bag]:
        if b not in bags_in_other_bags:
            bags_not_in_other_bags.add(b)
part1count = 0

important_bags = set()
def rec(bag):
    if bag in bags_not_in_other_bags:
        important_bags.add(bag)
    else:
        c = 0
        important_bags.add(bag)
        for b in graph[bag]:
            rec(b)

rec('shiny gold')
print(f"Part 1: {len(important_bags)-1}")


def rec2(bag):
    containedbags = bagswithnumsdict[bag]
    c = 0
    for bag_and_num in containedbags:
        b = list(bag_and_num.keys())[0]
        count = bag_and_num[b]

        if len(bagswithnumsdict[b]) == 0:
            c += count

        else:
            c += count + rec2(b) * count


    return c

print(f"Part 2: {rec2('shiny gold')}")

