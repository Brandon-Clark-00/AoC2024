direction =[-1,0]
stuck = 0
def get_new_dir(dir):
    global guard
    match(dir):
        case [1,0]:
            guard["icon"] = "<"
            return [0,-1]
        case [0,-1]:
            guard["icon"] = "^"
            return [-1,0]
        case [-1,0]:
            guard["icon"] = ">"
            return [0,1]
        case [0,1]:
            guard["icon"] = "v"
            return [1,0]
            
    

def find_guard(grid):
    i = 0
    for line in matrix:
        if "^" in line:
            return [i,line.index("^")]
        i+=1


def get_new_pos(pos,direction):
    pos[0] += direction[0]
    pos[1] += direction[1]
    return pos

def reverse(pos, direction):
    pos[0] += (direction[0]/-1)
    pos[1] += (direction[1]/-1)
    return pos

def route_guard(grid, guard):
    global stuck
    distinct:set =set()
    global direction
    height = len(grid)
    width = len(grid[0])
    while True:
            grid[int(guard["pos"][0])][int(guard["pos"][1])] = guard["icon"]
            temp = guard["pos"]
            newPos = get_new_pos(temp, direction)
            if newPos[0] >= height or newPos[0] < 0 or newPos[1] >= width or newPos[1]<0:
                print("The guard has left the area bro")
                print("The guard took " + str(guard["steps"]) + " steps")
                return guard
            elif grid[int(newPos[0])][int(newPos[1])] == "#":
                newPos = reverse(newPos,direction)
                direction = get_new_dir(direction)
                continue
            else:

                guard["pos"] = newPos
                guard["steps"] +=1
                distinct.add(tuple(newPos[:]))
       
            if grid[int(guard["pos"][0])][int(guard["pos"][1])] == guard["icon"] or guard["steps"] >10000:
                stuck+=1
                # for line in grid:
                #     print(line)
                return guard
                

file = open("Day6.txt","r")

matrix = []
for line in file:
    if line.__contains__("\n"):
            line = "".join(filter(lambda c: c != "\n", line))
    matrix.append(list(map(str, list(line))))

guard ={
    "pos": find_guard(matrix),
    "steps":0,
    "icon":"^"
}


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == find_guard(matrix):
            continue
        print(f"Y:{i} X:{j}")
        changeMat = [row[:] for row in matrix]
        changeMat[i][j] = "#"
        # for line in changeMat:
        #     print(line)
        guard = route_guard(changeMat,guard)
        changeMat =[]
        guard["pos"] = find_guard(matrix)
        guard["icon"] = "^"
        guard["steps"] = 0
        direction = [-1,0]
print(f"There are {stuck} number of possibilities")