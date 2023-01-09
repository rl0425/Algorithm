import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

num = int(input())

def allow(a, b, leftData, rightData, inputData):
    for up in range(rightData - 1, -1, -1):
        if (leftData, up, 0) in inputData:
            inputData.remove((leftData, up, 0))
            inputData.add((leftData, up, 1))
            allow(a, b, leftData, up, inputData)

        else:
            break

    for down in range(rightData + 1, b):
        if (leftData, down, 0) in inputData:
            inputData.remove((leftData, down, 0))
            inputData.add((leftData, down, 1))
            allow(a, b, leftData, down, inputData)

        else:
            break

    for left in range(leftData - 1, -1, -1):
        if (left, rightData, 0) in inputData:
            inputData.remove((left, rightData, 0))
            inputData.add((left, rightData, 1))
            allow(a, b, left, rightData, inputData)

        else:
            break

    for right in range(leftData + 1, a):
        if (right, rightData, 0) in inputData:
            inputData.remove((right, rightData, 0))
            inputData.add((right, rightData, 1))
            allow(a, b, right, rightData, inputData)

        else:
            break
    

for x in range(num):

    count = 0
    a, b, c = map(int,input().split())

    inputData = set()

    for y in range(c):
        e, f = map(int, input().split())

        inputData.add((e, f, 0))

    while len(inputData) != 0:
        data = inputData.pop()
        noCount = False

        allow(a, b, data[0], data[1], inputData)

        if data[2] == 0:
            count += 1

    print(count)