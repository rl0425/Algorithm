import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
inputData = []
max = 0

def func():
    global inputData
    global max

    for x in range(a):
        for y in range(b):
            temp = int(inputData[x][y])

            ffunc(x,y,1,temp,0)
            BequFunc(x,y)

def BequFunc(x,y):
    global inputData, max

    if x-1 >= 0 and y-1 >= 0 and y + 1 < b:
        alpha = int(inputData[x][y]) + int(inputData[x-1][y]) + int(inputData[x][y-1]) + int(inputData[x][y+1])
        if alpha > max:
            max = alpha
    if x-1 >= 0 and x+1 < a and y + 1 < b:
        alpha = int(inputData[x][y]) + int(inputData[x-1][y]) + int(inputData[x+1][y]) + int(inputData[x][y+1])
        if alpha > max:
            max = alpha
    if x+1 < a and y-1 >= 0 and y + 1 < b:
        alpha = int(inputData[x][y]) + int(inputData[x+1][y]) + int(inputData[x][y-1]) + int(inputData[x][y+1])
        if alpha > max:
            max = alpha
    if x-1 >= 0 and y-1 >= 0 and x + 1 < a:
        alpha = int(inputData[x][y]) + int(inputData[x-1][y]) + int(inputData[x][y-1]) + int(inputData[x+1][y])
        if alpha > max:
            max = alpha

    return;

def ffunc(x,y,count,sum, prev):
    global inputData, max
    global a,b

    if count == 4:
        if sum > max:
            max = sum
        return

    if x - 1 >= 0 and prev != 3:
        ffunc(x-1, y, count+1, int(sum) + int(inputData[x-1][y]), 1)

    if y + 1 < b and prev != 4:
        ffunc(x, y + 1, count + 1, int(sum) + int(inputData[x][y + 1]), 2)

    if x + 1 < a and prev != 1:
        ffunc(x + 1, y, count + 1, int(sum) + int(inputData[x + 1][y]), 3)

    if y - 1 >= 0 and prev != 2:
        ffunc(x, y-1, count + 1, int(sum) + int(inputData[x][y-1]), 4)

for x in range(a):
    inputData.append(input().rstrip().split())

func()

print(max)