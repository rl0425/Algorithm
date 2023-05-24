import sys
input = sys.stdin.readline

a = int(input())
inputData = []

for x in range(a):
    inputData.append(list(map(int, input().rstrip().split())))

for data in inputData:
    isAnswer = True

    while data[2] <= data[0]*data[1]:
        if (data[2] - data[3]) % data[1] == 0:
            print(data[2])
            isAnswer = False
            break
        else:
            data[2] += data[0]

    if isAnswer:
        print(-1)