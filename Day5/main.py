f = open("Day5\input", 'r')
lst = []
for line in f:
    word = line.rstrip(" \n")
    lst.append(word)
f.close()

# Part 1
id_lst = []
for seat in lst:
    row = 0
    step = 64
    for i in range(7):
        if seat[i] == "B":
            row += step
        step //= 2
    column = 0
    step = 4
    for j in range(7,10):
        if seat[j] == "R":
            column += step
        step //= 2
    id = row * 8 + column
    id_lst.append(id)
print(max(id_lst))

# Part 2
id_lst.sort()
for i in range(id_lst[0], id_lst[-1]):
    if i not in id_lst and i-1 in id_lst and i+1 in id_lst:
        print(i)
