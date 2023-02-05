a, b = map(int, input().split())

inputData = []
trueList = [[0 for _ in range(b)] for i in range(a)]

def bfs():
    trueList[0][0] = 1
    list = []
    list.append([0, 0])

    while len(list) != 0:
        [x, y] = list.pop(0)
        temp = []

        if x == a-1 and y == b-1:
            return trueList[x][y]

        if x-1 >= 0 and inputData[x-1][y] == str(1):
            temp.append([x-1, y])
        if x+1 < a and inputData[x+1][y] == str(1):
            temp.append([x+1, y])
        if y-1 >= 0 and inputData[x][y-1] == str(1):
            temp.append([x, y-1])
        if y+1 < b and inputData[x][y+1] == str(1):
            temp.append([x, y+1])

        for ele in temp:

            if trueList[ele[0]][ele[1]] == 0 or trueList[ele[0]][ele[1]] > trueList[x][y]+1:
                trueList[ele[0]][ele[1]] = trueList[x][y] + 1
                list.append([ele[0], ele[1]])


for x in range(a):
    inputData.append(input())

print(bfs())
