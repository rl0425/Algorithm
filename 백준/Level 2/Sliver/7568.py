a = int(input())
inputData = []
answer = []
count = 1

for x in range(a):
    inputData.append(list(map(int, input().split())))

for x in range(len(inputData)):
    for y in range(len(inputData)):
        if inputData[y][0] > inputData[x][0] and inputData[y][1] > inputData[x][1]:
            count += 1
    answer.append(count)

    count = 1

print(*answer)
