import re

f = open("Day6\input", 'r')
lst = []
dct = {}
PartOne = False
first = True
for line in f:
    word = line.rstrip(" \n")
    if word == "":
        lst.append(dct)
        dct = {}
        first = True
    else:
        if first == True or PartOne == True:
            for letter in word:
                dct[letter] = True
            first = False
        else:
            for letter in list(dct.keys()):
                if letter not in word:
                    dct.pop(letter)
lst.append(dct)
f.close()

# Part 1 & 2
count = 0
for i in lst:
    count += len(i)
print(count)

