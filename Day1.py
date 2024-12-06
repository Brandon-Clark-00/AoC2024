file = open("Day1.txt","r")

a = []
b = []
similarities = []

for line in file:
    a.append(line.split()[0])
    b.append(line.split()[1])


for numA in a:
    count = 0
    for numB in b:
        if numA == numB:
            count+=1
    similarities.append(int(count)*int(numA))
# print(a)
# print(b)
print(similarities)
print(sum(similarities))