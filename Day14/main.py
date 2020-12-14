f = open("Day14\input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n")
    words = word.split(" = ")
    if words[0] == "mask":
        lst.append((words[0], words[1]))
    else:
        lst.append((int(words[0].strip("me[]")), int(words[1])))
f.close()


# Part 1
def number_to_binary(nbr, bits):
    binary = ""
    for i in range(bits-1, -1, -1):
        if nbr >= 2**i: 
            nbr -= 2**i
            binary += "1"
        else: binary += "0"
    return binary

def binary_to_nbr(binary):
    nbr = 0
    for i in range(len(binary)):
        if binary[i] == "1": nbr += 2**(len(binary)-i-1)
    return nbr

def apply_mask(binary, mask):
    result = ""
    for i in range(len(binary)):
        if mask[i] == "X": result += binary[i]
        elif mask[i] == "1": result += "1"
        else: result += "0"
    return result

adress_space = {}
mask = ""

for instruction in lst:
    if instruction[0] == "mask": mask = instruction[1]
    else:
        adress_space[instruction[0]] = binary_to_nbr(apply_mask(number_to_binary(instruction[1], 36), mask))

final_sum = 0
for key, value in adress_space.items():
    final_sum += value
print(final_sum)

# Part 2
def memory_mask(binary, mask):
    all_adresses = []
    adress = ""
    for i in range(len(binary)):
        if mask[i] == "0": adress += binary[i]
        elif mask[i] == "1": adress += "1"
        else:
            if i < len(binary)-1:
                endings = memory_mask(binary[i+1:], mask[i+1:])
                for j in endings:
                    all_adresses.append(adress+"0"+j)
                    all_adresses.append(adress+"1"+j)
            else: 
                all_adresses.append(adress+"0")
                all_adresses.append(adress+"1")
            return all_adresses
    all_adresses.append(adress)
    return all_adresses

adress_space = {}
mask = ""

for instruction in lst:
    if instruction[0] == "mask": mask = instruction[1]
    else:
        for i in memory_mask(number_to_binary(instruction[0], 36), mask):
            adress_space[i] = instruction[1]

final_sum = 0
for key, value in adress_space.items():
    final_sum += value
print(final_sum)

