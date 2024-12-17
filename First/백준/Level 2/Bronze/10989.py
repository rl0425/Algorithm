import sys
input = sys.stdin.readline

num = int(input())
inputData = dict()

for x in range(num):

    data = int(input())

    if data in inputData:
        inputData[data] += 1
    else:
        inputData[data] = 1

inputData = sorted(inputData.items())

for x in inputData:
    for y in range(x[1]):
        print(x[0])


