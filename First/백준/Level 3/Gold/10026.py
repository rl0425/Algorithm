a = int(input())
inputData = []
flag = [[False for j in range(a)] for i in range(a)]

def bfs(array, type):
    count = 0
    for x in range(len(array)):
        for y in range(len(array)):
            if flag[x][y] != True:
                if type == "normal":
                    array = bfsFunc(x, y, array, array[x][y])
                if type == "sekyak":
                    if array[x][y] == "R" or array[x][y] == "G":
                        array = bfsFunc(x, y, array, ["R", "G"])
                    else:
                        array = bfsFunc(x, y, array, array[x][y])
                count += 1

    return count

def bfsFunc(x, y, array, color):
    queue = [(x,y)]

    while queue:
        num = queue.pop(0)
        if num[0]+1 < a and array[num[0]+1][num[1]] in color and flag[num[0]+1][num[1]] == False:
            flag[num[0]+1][num[1]] = True
            queue.append((num[0]+1, num[1]))

        if num[0]-1 >= 0 and array[num[0]-1][num[1]] in color and flag[num[0]-1][num[1]] == False:
            flag[num[0]-1][num[1]] = True
            queue.append((num[0]-1, num[1]))

        if num[1]+1 < a and array[num[0]][num[1]+1] in color and flag[num[0]][num[1]+1] == False:
            flag[num[0]][num[1]+1] = True
            queue.append((num[0], num[1] + 1))

        if num[1]-1 >= 0 and array[num[0]][num[1]-1] in color and flag[num[0]][num[1]-1] == False:
            flag[num[0]][num[1]-1] = True
            queue.append((num[0], num[1] - 1))

    return array

for x in range(a):
    inputData.append(input())

print(bfs(inputData, "normal"))
flag = [[False for j in range(a)] for i in range(a)]
print(bfs(inputData, "sekyak"))
