a = int(input())

inputList = []
trueList = []
answer = []

for x in range(a):
    inputList.append(input())

trueList = [[False for j in range(a)] for i in range(a)]

for x in range(a):
    for y in range(a):
        if int(inputList[x][y]) == int(1):
            trueList[x][y] = True

def search(x, y, num):
    trueList[x][y] = False
    num += 1

    if x-1 >= 0 and trueList[x-1][y]:
        num = search(x - 1, y, num)
    if x+1 < a and trueList[x+1][y]:
        num = search(x + 1, y, num)
    if y-1 >= 0 and trueList[x][y-1]:
        num = search(x, y - 1, num)
    if y+1 < a and trueList[x][y+1]:
        num = search(x, y + 1, num)

    return num

for x in range(len(trueList)):
    for y in range(len(trueList)):
        if trueList[x][y]:
            answer.append(search(x,y,0))

answer.sort()

print(len(answer))
print(*answer)