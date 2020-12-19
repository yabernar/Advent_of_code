f = open("Day19\input2", 'r')
all_rules = {}
all_msg = []
for line in f:
    word = line.rstrip("\n")
    if ":" in word:
        r = word.split(": ")
        if  "a" in r[1] or "b" in r[1]:
            all_rules[r[0]] = r[1][1]
        elif "|" in r[1]:
            options = r[1].split(" | ")
            all_rules[r[0]] = [options[0].split(" "), options[1].split(" ")]
        else:
            all_rules[r[0]] = [r[1].split(" ")]
    elif word != "":
        all_msg.append(word)
f.close()

# Part 1
def match_rule(rule, message):
    if message == "" and rule == []: return True
    if message == "" or rule == []: return False
    if all_rules[rule[0]] == "a":
        if message[0] == "a": return match_rule(rule[1:], message[1:])
        else: return False
    if all_rules[rule[0]] == "b":
        if message[0] == "b": return match_rule(rule[1:], message[1:])
        else: return False
    for i in range(len(all_rules[rule[0]])):
        if match_rule(all_rules[rule[0]][i]+rule[1:], message): return True
    return False


count = 0
for i in all_msg:
    if match_rule(["0"], i): count += 1
print(count)