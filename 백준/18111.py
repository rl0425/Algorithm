# pypy o

a,b,c = map(int, input().split())

inputData = []
data = []

for x in range(a):
    d = list(map(int, input().split()))

    inputData.append(d)

for x in inputData:
    for y in x:
        data.append(y)

has = c
time = 0
answer = dict()

for x in range(max(data), min(data)-1, -1):
    # 땅을 팔 경우
    for y in data:
        has += -(x - y)

        if x-y > 0:
            time += 1 * x-y
        elif x-y == 0:
            time += 0
        else :
            time += 2 * (y-x)

    if has >= 0:
        answer[x] = time

    has = c
    time = 0

answerMin = min(answer.values())

for key, value in answer.items():
    if value == answerMin:
        print(answerMin, key)
        break
