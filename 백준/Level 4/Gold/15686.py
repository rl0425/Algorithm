import itertools

a, b = map(int, input().split())
inputData = []

def geometry(array):
    minSum = 0
    newChicken = []

    for x in range(len(array)):
        for y in range(len(array)):
            if array[x][y] == str(2):
                newChicken.append((x,y))

    for x in houseList:
        min = 0
        for y in newChicken:
            distance = abs(x[0]-y[0]) + abs(x[1]-y[1])
            if min == 0:
                min = distance

            if min > distance:
                min = distance
        minSum += min

    return minSum

for x in range(a):
    inputData.append(input().split())

chickenList = []
houseList = []

for x in range(len(inputData)):
    for y in range(len(inputData)):
        if inputData[x][y] == str(2):
            chickenList.append((x, y))
        if inputData[x][y] == str(1):
            houseList.append((x, y))

comb = itertools.combinations(chickenList, len(chickenList) - b)

distanceMin = 0
for c in comb:
    newList = [arr[:] for arr in inputData]
    for x in c:
        newList[x[0]][x[1]] = 0

    distance = geometry(newList)
    if distanceMin == 0:
        distanceMin = distance

    if distanceMin > distance:
        distanceMin = distance

print(distanceMin)
