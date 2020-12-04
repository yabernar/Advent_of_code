import re

f = open("Day4\input", 'r')
lst = []
dct = {}
for line in f:
    word = line.rstrip(" \n")
    if word == "":
        lst.append(dct)
        dct = {}
    else:
        all_fields = word.split(" ")
        for field in all_fields:
            key, value = field.split(":")
            dct[key] = value
lst.append(dct)
f.close()

# Part 1
valid_nbr = 0
for p in lst:
    if (len(p) == 8) or (len(p) == 7 and "cid" not in p):
        valid_nbr += 1
print(valid_nbr)

# Part 2
valid_nbr = 0
for p in lst:
    if (len(p) == 8) or (len(p) == 7 and "cid" not in p):
        byr = 1920 <= int(p["byr"]) <= 2002
        iyr = 2010 <= int(p["iyr"]) <= 2020
        eyr = 2020 <= int(p["eyr"]) <= 2030
        cm = p["hgt"][-2:] == "cm" and 150 <= int(p["hgt"][:-2]) <= 193
        inc = p["hgt"][-2:] == "in" and 59 <= int(p["hgt"][:-2]) <= 76
        hgt = cm or inc
        hcl = p["hcl"][0] == "#" and len(p["hcl"]) == 7 and re.search("[0-9a-f]{6}",p["hcl"])
        ecl = p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        pid = len(p["pid"]) == 9 and p["pid"].isdigit() 
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid_nbr += 1
print(valid_nbr)