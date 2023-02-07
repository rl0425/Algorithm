a = int(input())
inputList = []
d = [0 for i in range(1, 1001)]
answer = 0

for x in range(a):
    inputList.append(list(map(int, input().split())))

for x in inputList[0]:
    d[x] = x

for x in range(1, len(inputList)):
    d[inputList[x][0]] = inputList[x][0] + min(d[inputList[x-1][1]], d[inputList[x-1][2]])
    d[inputList[x][1]] = inputList[x][1] + min(d[inputList[x-1][0]], d[inputList[x-1][2]])
    d[inputList[x][2]] = inputList[x][2] + min(d[inputList[x-1][0]], d[inputList[x-1][1]])


    if x == len(inputList) - 1:
        answer = min(d[inputList[x][0]], d[inputList[x][1]], d[inputList[x][2]])


print(answer)