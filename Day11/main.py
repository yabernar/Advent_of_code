import copy
 
f = open("Day11\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append(list(word))
f.close()

Part2 = True

# Part 1
def check_seat(i, j, offset_i, offset_j):
    if 0 <= i+offset_i <= len(lst)-1 and 0 <= j+offset_j <= len(lst[0])-1:
        if lst[i+offset_i][j+offset_j] == "#":
            return 1
        if lst[i+offset_i][j+offset_j] == "." and Part2:
            return check_seat(i+offset_i, j+offset_j, offset_i, offset_j)
    return 0


def count_occupied_seats(i, j):
    return  check_seat(i, j, 0, 1) + check_seat(i, j, 0, -1) + check_seat(i, j, 1, 0) + check_seat(i, j, -1, 0) +\
            check_seat(i, j, 1, 1) + check_seat(i, j, 1, -1) + check_seat(i, j, -1, 1) + check_seat(i, j, -1, -1)

def update():
    global lst
    hasChanged = False
    new_lst = copy.deepcopy(lst)
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 'L' and count_occupied_seats(i,j) == 0:
                new_lst[i][j] = '#'
                hasChanged = True
            if lst[i][j] == '#' and count_occupied_seats(i,j) >= 5:
                new_lst[i][j] = 'L'
                hasChanged = True
    lst = new_lst
    return hasChanged

# Part 1 & 2
while update():
    pass
final_occupied_seats = 0
for i in lst:
    for j in i:
        if j == "#":
            final_occupied_seats += 1
print(final_occupied_seats)