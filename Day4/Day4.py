import math
directions = [(3, 0), (-3, 0), (0, 3), (0, -3), (3, 3), (3, -3), (-3, 3), (-3, -3)]
dirnames =["Down", "Up","Right","Left","Down-Right","Down-Left","Up-Right","Up-Left"]

def findWord(grid, word:str, directions, mX,mY, mas:bool):
    count = 0
    templist: list = []
    temp =""
    print(mX)
    print(mY)
    for y in range(0,mY):
        for x in range(0,mX):
            for dirs in directions:
                dX = dirs[1]
                dY = dirs[0]
                if mas and (dX == 0 or dY == 0):
                    continue
                if x+dX > mX or y+dY > mY or x+dX <-1 or y+dY <-1:
                    temp =""
                    continue
                else:
                    yStep: int = find_yStep(y,dY)
                    xStep: int = find_xStep(x,dX)
                    i = x
                    j = y
                    while j != y+dY or i != x+dX:
                        temp+= grid[j][i]
                        if j == y+dY:
                            yStep = 0
                        if i == x+dX:
                            xStep = 0
                        j+=yStep
                        i+=xStep
                        if j == y+dY and i == x+dX:
                            break 
                    if temp == word:
                        count+=1
                        templist.append(((x+(find_xStep(x,dX))),(y+find_yStep(y,dY))))
                    temp =""
    print(f"Duplicates =  {find_duplicates(templist)}")
                    
    return count

def find_duplicates(inputList:list):
    dupList:list =[]
    count = 0
    print(inputList)
    while len(inputList) != 0:
        # print(inputList)
        current = inputList.pop()
        if current in inputList: 
            count+=1
            dupList.append(current)
            inputList.remove(current)
        # print(inputList)
    print(dupList)
    return count


def find_yStep(y,dY):
    yStep = 1
    if y + dY < y:
        yStep = -1
    elif y+ dY == y:
        yStep = 0
    return yStep

def find_xStep(x,dX):
    xStep = 1
    if x + dX < x:
            xStep = -1
    elif x+dX == x:
        xStep = 0
    return xStep

def checkCross(pointList):
    for i in range(0,len(pointList)):
        for j in range(0, len(pointList)):
            print(pointList[i][j])
        




file = open("Day4.txt","r")



matrix = [list(map(str, list(line))) for line in file]

for line in matrix:
    if line.__contains__("\n"):
        line.remove("\n")
 
print(findWord(matrix,"MAS",directions,len(matrix[0]),len(matrix), True))
