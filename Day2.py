def checksorted(line: list):
    line = list(map(int,line))
    if line == sorted(line) or line == (sorted(line, reverse=True)):
        return True
    else:
        return False
def checkDiff(a,b):
    check = int(a)-int(b)
    if check == 0:
        return False
    elif check in range(-3,4):
        return True
    else:
        return False
def checkLevel(line: list):
    for i in range(len(line)-1):
        if(not checkDiff(line[i], line[i+1]) ):
           return False
    return True

file = open("Day2.txt")
count = 0
i = 0
for line in file:
    # if i> 30: break
    level = checkLevel(line.split())
    is_sorted = checksorted(line.split())
    if(level and is_sorted):
        print("Safe")
        count+=1
    else:
        for i in range(len(line.split())):
            print(i)
            temp = line.split()
            del temp[i]
            level = checkLevel(temp)
            is_sorted = checksorted(temp)
            if(level and is_sorted):
                print("Safe")
                count+=1
                break
        print("Unsafe")
    i+=1

print("Count is equal to: " + str(count))
   