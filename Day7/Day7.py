


file = open("./Day7/Test7.txt")

calculations = []

for line in file:
    calculations.append(line.rstrip().split(":"))

for line in calculations:
    line[1] = line[1].lstrip(" ").split(" ")

for line in calculations:
    print(line)