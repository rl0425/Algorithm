a,b,c = map(int,input().split())

inputList = set()

for x in range(b):
    d, e = map(int, input().split())
    inputList.add((d,e))

loopList = set()
bottomList = set()
numberList = set()

dfs = []
bfs = []

def dfsFunc(x):
    hadList = []

    for y in inputList:
        if y[0] == x and y[1] not in dfs:
            hadList.append(y)

    if len(hadList) > 0:
        hadList = sorted(hadList, key= lambda x: x[1])
        alpha = hadList[0]

        if alpha[1] not in dfs:
            dfs.append(alpha[1])

        inputList.remove(alpha)
        dfsFunc(alpha[1])

    else:
        return

for x in inputList:
    bottomList.add(x[1])

for x in inputList:
    if x[0] not in bottomList:
        loopList.add(x[0])

for x in inputList:
    numberList.add(x[0])
    numberList.add(x[1])


dfs.append(c)

while True:
    for x in loopList:
        if x not in dfs:
            dfs.append(x)

        dfsFunc(x)

    if len(dfs) == len(numberList):
        break

while True:


print("dfs = ", dfs)

