f = open("Day13\input", 'r')
depart = int(f.readline().rstrip("\n"))
buses = f.readline().rstrip("\n").split(",")
f.close()

bus_id = []
offset = []
for i in range(len(buses)):
    if buses[i] != "x":
        bus_id.append(int(buses[i]))
        offset.append(i)

# Part 1
found = None
wait = -1
while not found:
    wait += 1
    for i in bus_id:
        if (depart+wait)%i == 0: found = i
print(found, wait, found*wait)

# Part 2
def find_timestamp(id1, offset1, id2, offset2):
    found = None
    timestamp = id1+offset1
    while not found:
        if (timestamp + offset2)%id2 == 0: found = timestamp
        else : timestamp += id1
    return id1*id2, found

id = bus_id[0]
off = offset[0]
for i in range(1, len(bus_id)):
    print(id, off)
    id, off = find_timestamp(id, off, bus_id[i], offset[i])

print(id, off)