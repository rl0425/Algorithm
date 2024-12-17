a = int(input())
inputData = [[0] for _ in range(a)]
answerData = [[0 for _ in range(a)] for _ in range(a)]

def hangyeol(inputData):
    global answerData

    for x in range(len(inputData)):
        for y in range(len(inputData)):
            if inputData[x][y] == "1":
                answerData[x][y] = "1"
                func(x, y)

def func(start, y):
    global inputData, answerData

    if start != y:
        for x in range(len(inputData)):
            if inputData[y][x] == "1":
                if answerData[start][x] != "1":
                    answerData[start][x] = "1"
                    func(start, x)

for x in range(a):
    inputData[x] = input().split()

hangyeol(inputData)

for x in range(len(answerData)):
    print(*answerData[x])