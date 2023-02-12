a,b = map(int, input().split())

inputData = []

def BFS(array):
    passTomato = []
    newTomato = []
    num = 0

    for x in range(b):
        for y in range(a):
            if array[x][y] == 1:
                passTomato.append((x, y))

    while True:
        for tomato in passTomato:
            if tomato[0]+1 < b and array[tomato[0]+1][tomato[1]] == 0:
                newTomato.append((tomato[0] + 1, tomato[1]))
                array[tomato[0] + 1][tomato[1]] = 1
            if tomato[0]-1 >= 0 and array[tomato[0]-1][tomato[1]] == 0:
                newTomato.append((tomato[0] - 1, tomato[1]))
                array[tomato[0] - 1][tomato[1]] = 1
            if tomato[1]+1 < a and array[tomato[0]][tomato[1]+1] == 0:
                newTomato.append((tomato[0], tomato[1]+1))
                array[tomato[0]][tomato[1] + 1] = 1
            if tomato[1]-1 >= 0 and array[tomato[0]][tomato[1]-1] == 0:
                newTomato.append((tomato[0], tomato[1]-1))
                array[tomato[0]][tomato[1] - 1] = 1

        passTomato = list(newTomato)
        newTomato = []

        if len(passTomato) == 0:
            for x in range(b):
                if 0 in array[x]:
                    return -1
            return num
        else:
            num += 1

for x in range(b):
    inputData.append(list(map(int,input().split())))

print(BFS(inputData))

