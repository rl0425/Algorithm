import sys

input = sys.stdin.readline

a, b = map(int, input().split())
inputData = {}

visited = []
numList = [i for i in range(1,a+1)]

count = 0

def dfs(array, start):
    dfsArr = [start]

    while dfsArr:
        data = dfsArr.pop()

        if data not in visited:
            visited.append(data)
            if data in numList:
                numList.remove(data)

            if data in array:
                temp = list(set(array[data]) - set(visited))
                dfsArr += temp

for x in range(b):
    c, d = map(int, input().split())

    if c not in inputData:
        inputData[c] = [d]
    else:
        inputData[c].append(d)

    if d not in inputData:
        inputData[d] = [c]
    else:
        inputData[d].append(c)

while numList:
    dfs(inputData, numList[0])

    count += 1

print(count)