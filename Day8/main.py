import re

f = open("Day8\input", 'r')
code = []
for line in f:
    word = line.rstrip("\n")
    inst, value = word.split(" ")
    code.append((inst,int(value)))
f.close()

def run(skip):
    acc = 0
    instruction = 0
    skip_cnt = 1
    visited_lines = []
    while instruction not in visited_lines and instruction < len(code):
        visited_lines.append(instruction)
        if code[instruction][0] == "acc":
            acc += code[instruction][1]
            instruction += 1
        elif code[instruction][0] == "jmp":
            if skip == skip_cnt:
                instruction += 1
            else:
                instruction += code[instruction][1]
            skip_cnt += 1
        elif code[instruction][0] == "nop":
            if skip == skip_cnt:
                instruction += code[instruction][1]               
            else:
                instruction += 1
            skip_cnt += 1
    return instruction == len(code), acc

# Part 1
print("Part 1 :", run(0))

# Part 2
i = 1
stop = False
while not stop:
    stop, acc = run(i)
    print(i, stop, acc)
    i += 1