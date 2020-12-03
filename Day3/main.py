f = open("Day3\input", 'r')
lst = []
for line in f:
    word = line.rstrip(" \n")
    lst.append(word)
f.close()

# Part 1
trees = 0
for y in range(1, len(lst)):
    x = (y*3)%len(lst[0])
    if(lst[y][x] == "#"):
        trees += 1
print(trees)


# Part 2
def check_slope(right, down):
    trees = 0
    for y in range(down, len(lst), down):
        x = ((y//down)*right)%len(lst[0])
        if(lst[y][x] == "#"):
            trees += 1
    return trees

res = check_slope(1,1) * check_slope(3,1) * check_slope(5,1) * check_slope(7,1) * check_slope(1,2)
print(res)