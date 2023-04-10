import itertools

a, b = map(int, input().split())
inputData = []

def BFS(array):
    passTomato = []
    newTomato = []

    for x in range(a):
        for y in range(b):
            if array[x][y] == 2:
                passTomato.append((x, y))

    while True:
        for tomato in passTomato:
            if tomato[0]+1 < a and array[tomato[0]+1][tomato[1]] == 0:
                newTomato.append((tomato[0] + 1, tomato[1]))
                array[tomato[0] + 1][tomato[1]] = 2
            if tomato[0]-1 >= 0 and array[tomato[0]-1][tomato[1]] == 0:
                newTomato.append((tomato[0] - 1, tomato[1]))
                array[tomato[0] - 1][tomato[1]] = 2
            if tomato[1]+1 < b and array[tomato[0]][tomato[1]+1] == 0:
                newTomato.append((tomato[0], tomato[1]+1))
                array[tomato[0]][tomato[1] + 1] = 2
            if tomato[1]-1 >= 0 and array[tomato[0]][tomato[1]-1] == 0:
                newTomato.append((tomato[0], tomato[1]-1))
                array[tomato[0]][tomato[1] - 1] = 2

        passTomato = list(newTomato)
        newTomato = []

        if len(passTomato) == 0:
            count = 0
            for row in array:
                for element in row:
                    if element == 0:
                        count += 1
            return count

for x in range(a):
    inputData.append(list(map(int, input().split())))

zero_indices = []

for i in range(len(inputData)):
    for j in range(len(inputData[i])):
        if inputData[i][j] == 0:
            zero_indices.append((i, j))

combinations = itertools.combinations(zero_indices, 3)
maxNum = 0

for combination in combinations:
    copied = [[x for x in row] for row in inputData]
    for i, j in combination:
        copied[i][j] = 1

    count = BFS(copied)
    if maxNum < count:
        maxNum = count

print(maxNum)
