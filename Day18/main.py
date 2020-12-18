f = open("Day18\input", 'r')
op_list = []
for line in f:
    word = line.rstrip("\n")
    word = word.replace(" ", "")
    lst = []
    for i in word:
        if i.isnumeric(): lst.append(int(i))
        else: lst.append(i)
    op_list.append(lst)
f.close()

Part2 = True

# Part 1 & 2
def solve(operation):
    if ")" in operation:
        start = operation.index(")")
        end = operation.index("(")
        while operation[start:end+1].count(")") != operation[start:end+1].count("("): end = operation.index("(", end+1)
        return solve(operation[0:start] + [solve(operation[start+1:end])] + operation[end+1:])
    if Part2 and "*" in operation:
        pos = operation.index("*")
        return solve(operation[0:pos]) * solve(operation[pos+1:])
    if len(operation) == 1: return operation[0]
    if operation[1] == "+": return operation[0] + solve(operation[2:])
    if not(Part2) and operation[1] == "*": return operation[0] * solve(operation[2:])

res = 0
for i in op_list:
    i.reverse()
    res += solve(i)
print(res)