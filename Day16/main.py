f = open("Day16\input", 'r')
fields = {}
for i in range(20):
    line = f.readline().rstrip("\n")
    key, values = line.split(":")
    values = values.split(" or ")
    values[0] = values[0].split("-")
    values[1] = values[1].split("-")
    fields[key] = [int(values[0][0]), int(values[0][1]), int(values[1][0]), int(values[1][1])]

f.readlines(2)
own_ticket = f.readline().rstrip("\n").split(",")
for i in range(len(own_ticket)): own_ticket[i] = int(own_ticket[i])

f.readlines(2)
other_tickets = []
for line in f:
    t = line.rstrip("\n").split(",")
    for i in range(len(t)): t[i] = int(t[i])
    other_tickets.append(t)

# Part 1
invalid_values = []
valid_tickets = []
for ticket in other_tickets:
    valid_t = True
    for field in ticket:
        valid = False
        for key, value in fields.items():
            if value[0] <= field <= value[1] or value[2] <= field <= value[3]: valid = True
        if not valid:
            invalid_values.append(field)
            valid_t = False
    if valid_t:
        valid_tickets.append(ticket)
print(sum(invalid_values))

# Part 2

field_to_position = {}
for key, value in fields.items():
    positions = []
    for i in range(len(valid_tickets[0])):
        valid = True
        for ticket in valid_tickets:
            if not(value[0] <= ticket[i] <= value[1] or value[2] <= ticket[i] <= value[3]): 
                valid = False
        if valid:
            positions.append(i)
    field_to_position[key] = positions

final = {}
for i in range(len(field_to_position)):
    for key, value in field_to_position.items():
        if(len(value) == 1):
            position = value[0]
            final[key] = position
            for k, v in field_to_position.items():
                v.remove(position)
                field_to_position[k] = v
            del field_to_position[key]
            break

print(final)
res = 1
for k,v in final.items():
    if "departure" in k:
        res *= own_ticket[v]
print(res)
