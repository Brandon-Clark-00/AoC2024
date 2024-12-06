import re
total = 0
enabled = True

def findall_regex(input_text, regex):
    pattern = re.compile(regex, re.IGNORECASE)
    return pattern.findall(input_text)

def match_regex(input_text, regex):
    pattern = re.compile(regex, re.IGNORECASE)
    return pattern.search(input_text)

file = open("Day3.txt","r")


for line in file:
    calculations = findall_regex(line, "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)")
    # print(calculations)
    for calc in calculations:
        t = match_regex(calc, "do\(\)|don't\(\)")
        if t != None:
            if t.group() == "don't()":
                enabled = False
            else:
                enabled = True
            continue
        if enabled:
            w = findall_regex(calc,"\d.*\d")[0].split(",")
            total+= (int(w[0]) * int(w[1]))


print(total)