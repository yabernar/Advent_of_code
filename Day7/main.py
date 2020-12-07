import re

f = open("Day7\input", 'r')
dct = {}
for line in f:
    word = line.rstrip(".\n")
    color, contain = word.split(" bags contain ")
    dct[color] = []
    inside = contain.split(",")
    inside_dct = {}
    for i in inside:
        i = i.strip(" ")
        rule = i.split(" ")
        if rule[0] != "no":
            inside_dct["nbr"] = int(rule[0])
            inside_dct["color"] = rule[1]+" "+rule[2]
            dct[color].append(inside_dct)
            inside_dct = {}
f.close()

# Part 1
shiny_containers = []

def holding_bags(color):
    for bag_color, inside in dct.items():
        for contained in inside:
            if contained["color"] == color:
                if bag_color not in shiny_containers:
                    shiny_containers.append(bag_color)
                    holding_bags(bag_color)

holding_bags("shiny gold")
print(shiny_containers, len(shiny_containers))

# Part 2
def included_bag(color):
    inside = dct[color]
    nbr = 1
    for bag in inside:
        nbr += bag["nbr"] * included_bag(bag["color"])
    return nbr

print(included_bag("shiny gold")-1)
