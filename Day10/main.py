f = open("Day10\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(int(word))
f.close()

# Part 1
lst.sort()
last = 0
diff = [0, 0, 0, 0]
for i in range(len(lst)):
    d = lst[i] - last
    last = lst[i]
    diff[d] += 1
diff[3] += 1
print(diff[1] * diff[3])

# Part 2
paths = [0]*len(lst)
paths[0] = 1
paths[1] = 2
paths[2] = 4
for i in range(3, len(lst)):
    paths[i] += paths[i-1]
    if lst[i]-lst[i-2] <= 3:
        paths[i] += paths[i-2]
        if lst[i]-lst[i-3] <= 3:
            paths[i] += paths[i-3]
print(paths[-1])