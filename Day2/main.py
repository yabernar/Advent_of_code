input = open("Day2\input", 'r')
lst = []
for x in input:
    smin, _, line = x.partition("-")
    smax, _, line = line.partition(" ")
    letter, _, line = line.partition(":")
    word = line.rstrip(" \n")
    dct = {"min": int(smin), "max": int(smax), "letter": letter, "word": word}
    lst.append(dct)
input.close()

# Part 1
valid = 0
for dct in lst:
    nb = dct["word"].count(dct["letter"])
    if nb >= dct["min"] and nb <= dct["max"]:
        valid += 1
print("Part1 :", valid, "out of", len(lst))

# Part 2
valid = 0
for dct in lst:
    wrd = dct["word"]
    ltr = dct["letter"]
    if (ltr == wrd[dct["min"]]) ^ (ltr == wrd[dct["max"]]):
        valid += 1
print("Part2 :", valid, "out of", len(lst))

