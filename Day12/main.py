f = open("Day12\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    lst.append((word[0], int(word[1:])))
f.close()

# Part 1
orientation = 90
pos = [0, 0]
for i in lst:
    if i[0] == "N": pos[1] += i[1]
    elif i[0] == "S": pos[1] -= i[1]
    elif i[0] == "E": pos[0] += i[1]
    elif i[0] == "W": pos[0] -= i[1]
    elif i[0] == "R": orientation = (orientation + i[1])%360
    elif i[0] == "L": orientation = (orientation - i[1]+360)%360
    elif i[0] == "F": 
        if orientation == 0: pos[1] += i[1]
        elif orientation == 90: pos[0] += i[1]
        elif orientation == 180: pos[1] -= i[1]
        elif orientation == 270: pos[0] -= i[1]
print(pos, abs(pos[0])+abs(pos[1]))


# Part 2
ship = [0, 0]
wayptn = [10, 1]
rotation = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
for i in lst:
    if i[0] == "N": wayptn[1] += i[1]
    elif i[0] == "S": wayptn[1] -= i[1]
    elif i[0] == "E": wayptn[0] += i[1]
    elif i[0] == "W": wayptn[0] -= i[1]
    elif i[0] == "R": wayptn = [wayptn[(i[1]//90)%2]*rotation[i[1]//90][0], wayptn[(i[1]//90+1)%2]*rotation[i[1]//90][1]]
    elif i[0] == "L": wayptn = [wayptn[((360-i[1])//90)%2]*rotation[(360-i[1])//90][0], wayptn[((360-i[1])//90+1)%2]*rotation[(360-i[1])//90][1]]
    elif i[0] == "F": ship = [ship[0]+i[1]*wayptn[0], ship[1]+i[1]*wayptn[1]]
print(ship, abs(ship[0])+abs(ship[1]))