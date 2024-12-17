a = int(input())
inputList = []
d = [[0] * 3 for _ in range(a)]
answer = 0

for x in range(a):
    inputList.append(list(map(int, input().split())))

for x in range(len(inputList[0])):
    d[0][x] = inputList[0][x]

for x in range(1, len(inputList)):
    d[x][0] = inputList[x][0] + min(d[x-1][1], d[x-1][2])
    d[x][1] = inputList[x][1] + min(d[x-1][0], d[x-1][2])
    d[x][2] = inputList[x][2] + min(d[x-1][0], d[x-1][1])

    if x == len(inputList) - 1:
        answer = min(d[x][0], d[x][1], d[x][2])

print(answer)