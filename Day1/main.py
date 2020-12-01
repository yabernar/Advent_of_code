import pathlib

input = open("Day1\input.txt", 'r')
lst = []
for x in input:
    lst.append(int(x))
input.close()

for i in range(len(lst)):
    for j in range(i, len(lst)):
        for k in range(j, len(lst)):
            if lst[i] + lst[j] + lst[k] == 2020:
                print(lst[i], lst[j], lst[k], ":", lst[i]*lst[j]*lst[k])