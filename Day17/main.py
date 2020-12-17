import copy
 
f = open("Day17\input", 'r')
board = []
for line in f:
    word = line.rstrip("\n")
    lst = []
    for letter in word:
       lst.append([letter]) 
    board.append(lst)
f.close()

# Part 1
def count_active(j, k, l, board):
    count = 0
    for m in range(j-1, j+2):
        for n in range(k-1, k+2):
            for o in range(l-1, l+2):
                if not(m == j and n == k and o == l) and 1 <= m <= x-2 and 1 <= n <= y-2 and 1 <= o <= z-2 and board[m-1][n-1][o-1] == "#":
                    count += 1
    # print(j,k,l,"=",count)
    return count

x, y, z = len(board), len(board[0]), len(board[0][0])
for i in range(6):
    x, y, z = x+2, y+2, z+2
    new_board = []
    for j in range(x):
        line = []
        for k in range(y):
            line.append(["."]*z)
        new_board.append(line)
    for j in range(x):
        for k in range(y):
            for l in range(z):
                if 1 <= j <= x-2 and 1 <= k <= y-2 and 1 <= l <= z-2 and board[j-1][k-1][l-1] == "#" and 2 <= count_active(j, k, l, board) <= 3:
                    new_board[j][k][l] = "#"
                elif count_active(j, k, l, board) == 3:
                    new_board[j][k][l] = "#"
    board = new_board

res = 0
for i in new_board:
    for j in i:
        for k in j:
            if k == "#": res += 1
print(res)
