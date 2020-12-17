import copy
 
f = open("Day17\input", 'r')
board = []
for line in f:
    word = line.rstrip("\n")
    lst = []
    for letter in word:
       lst.append([[letter]]) 
    board.append(lst)
f.close()

# Part 1 & 2
def count_active(j, k, l, m, board):
    count = 0
    for n in range(j-1, j+2):
        for o in range(k-1, k+2):
            for p in range(l-1, l+2):
                for q in range(m-1, m+2):
                    if not(n == j and o == k and p == l and q == m) and 1 <= n <= x-2 and 1 <= o <= y-2 and 1 <= p <= z-2 and 1 <= q <= w-2 and board[n-1][o-1][p-1][q-1] == "#":
                        count += 1
    # print(j,k,l,"=",count)
    return count

x, y, z, w = len(board), len(board[0]), len(board[0][0]), len(board[0][0][0])
for i in range(6):
    x, y, z, w = x+2, y+2, z+2, w+2
    new_board = []
    for j in range(x):
        line = []
        for k in range(y):
            depth = []
            for l in range(z):
                depth.append(["."]*w)
            line.append(depth)
        new_board.append(line)
    for j in range(x):
        for k in range(y):
            for l in range(z):
                for m in range(w):
                    if 1 <= j <= x-2 and 1 <= k <= y-2 and 1 <= l <= z-2 and 1 <= m <= w-2 and board[j-1][k-1][l-1][m-1] == "#" and 2 <= count_active(j, k, l, m, board) <= 3:
                        new_board[j][k][l][m] = "#"
                    elif count_active(j, k, l, m, board) == 3:
                        new_board[j][k][l][m] = "#"
    board = new_board
    
for i in new_board:
    for j in i:
        for k in j:
            for l in k:
                if l == "#": res += 1
print(res)
