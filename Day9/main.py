f = open("Day9\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(int(word))
f.close()

# Part 1
invalid_nbr = 0
for i in range(25, len(lst)):
    valid = False
    for j in range(i-25, i-1):
        for k in range(j+1, i):
            if lst[j] + lst[k] == lst[i]:
                valid = True
    if not valid:
        print(lst[i])
        invalid_nbr = lst[i]
        break

# Part 2
for i in range(len(lst)):
    j = i+1
    while sum(lst[i:j]) < invalid_nbr:
        j += 1
    if sum(lst[i:j]) == invalid_nbr:
        mini = min(lst[i:j])
        maxi = max(lst[i:j])
        print(mini+maxi)
        break