a,b = map(int,input().split())

inputList = [0 for _ in range(a)]
goal = ""
min = 0

def func(x, y, count, prev):
    global inputList, min

    if x == goal[0] and y == goal[1]:
        if min < count:
            min = count
        return min;

    if inputList[x][y] == 0:
        return 0

    print("goal[0] =", goal[0])
    print("x = ", x)
    print("goal[1] =", goal[1])
    print("y = ", y)

    print("count = ", count)
    print("#######################")

    if x-1 >= 0 and prev != 3:
        if x-1 == int(goal[0]) and y == int(goal[1]):
            if min < count:
                min = count
            return min;
        elif inputList[x-1][y] != 0:
            func(x-1, y, count+1, 1)
    if x+1 < a and prev != 1:
        if x+1 == int(goal[0]) and y == int(goal[1]):
            if min < count:
                min = count
            return min;
        elif inputList[x+1][y] != 0:
            func(x+1, y, count+1, 3)
    if y-1 >= 0 and prev != 4:
        if x == int(goal[0]) and y-1 == int(goal[1]):
            if min < count:
                min = count
            return min;
        elif inputList[x][y-1] != 0:
            func(x, y-1, count+1, 2)
    if y+1 < b and prev != 2:
        if x == int(goal[0]) and y+1 == int(goal[1]):
            if min < count:
                min = count
            return min;
        elif inputList[x][y+1] != 0:
            func(x, y+1, count+1, 4)

    return min;

for x in range(a):
    inputList[x] = list(map(int, input().split()))

for x in range(a):
    for y in range(b):
        if inputList[x][y] == 2:
            goal = [x, y]

for x in range(a):
    for y in range(b):
        inputList[x][y] = func(x,y,0, 0)
        print("################################################################inputList[x][y] = ", inputList[x][y])
        print("################################################################inputList[x][y] = ", inputList[x][y])
        print("################################################################inputList[x][y] = ", inputList[x][y])
        min = 0



print(inputList)