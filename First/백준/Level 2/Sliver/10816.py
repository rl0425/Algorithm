n = int(input())
nNum = list(map(int, input().split()))
m = int(input())
mNum = list(map(int, input().split()))

nDict = dict()
answer = []

for x in nNum:
    if x in nDict:
        nDict[x] += 1
    else:
        nDict[x] = 1

for x in mNum:
    if x in nDict:
        answer.append(nDict[x])
    else:
        answer.append(0)

print(*answer)

