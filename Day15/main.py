f = open("Day15\input", 'r')
lst = []
nbrs = f.readline().rstrip("\n").split(",")
for i in nbrs:
    lst.append(int(i))
f.close()

print(lst)

# Part 1 & 2
spoken = {}
next_spoken = lst[0]
for i in range(1, 30000000):
    last_time = i - spoken[next_spoken]
    spoken[next_spoken] = i
    if i < len(lst): next_spoken = lst[i]
    elif next_spoken in spoken.keys(): next_spoken = last_time
    else: next_spoken = 0

print(next_spoken)