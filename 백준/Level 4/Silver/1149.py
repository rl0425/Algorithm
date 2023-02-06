a = int(input())
inputList = []
d = [0] * 1000001

sum = 0
notIndex = -1

for x in range(a):
    inputList.append(input().split())

if inputList[0][0] > inputList[0][1]:
    if inputList[0][1] > inputList[0][2]:
        d[inputList[0][2]] = inputList[0][2]
        notIndex = 2
    else:
        d[inputList[0][1]] = inputList[0][1]
        notIndex = 1
elif inputList[0][0] > inputList[0][2]:
    d[inputList[0][2]] = inputList[0][2]
    notIndex = 2
else:
    d[inputList[0][0]] = inputList[0][0]
    notIndex = 0

for x in range(1, len(inputList)):
    if notIndex == 0:
        min(d[inputList[x][1]], d[inputList[x][2]])


