direction =[-1,0]

def get_new_dir(dir):
    match(dir):
        case [1,0]:
            return [0,-1]
        case [0,-1]:
            return [-1,0]
        case [-1,0]:
            return [0,1]
        case [0,1]:
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
    distinct:set =set()
    global direction
    height = len(grid)
    width = len(grid[0])
    while True:
        temp = guard["pos"]
        newPos = get_new_pos(temp, direction)
        if newPos[0] >= height or newPos[0] < 0 or newPos[1] >= width or newPos[1]<0:
            print("The guard has left the area bro")
            print(f"The guard covered these tiles: {distinct}")
            print(f"{len(distinct)} distinct tiles")
            return guard
        elif grid[int(newPos[0])][int(newPos[1])] == "#":
            newPos = reverse(newPos,direction)
            direction = get_new_dir(direction)
            continue
        else:
            guard["pos"] = newPos
            guard["steps"] +=1
            distinct.add(tuple(newPos[:]))
    


file = open("Day6.txt","r")

# print(file)
matrix = [list(map(str, list(line))) for line in file]
guard ={
    "pos": find_guard(matrix),
    "steps":0
}

guard = route_guard(matrix,guard)
print(guard["steps"])