import sys
input = sys.stdin.readline

a = int(input())
aList = []
answer = []
num = dict()

for x in range(a):
    inpu = int(input())

    aList.append(inpu)
    num[inpu] = 0

aList.sort()

answer.append(round(sum(aList)/len(aList)))
answer.append(aList[int(len(aList)/2)])

for x in range(len(aList)):
    if num[aList[x]]:
        num[aList[x]] += 1
    else:
        num[aList[x]] = 1

numValue = num.values()

maxValue = max(numValue)
keyList = []

for key, value in num.items():
    if value == maxValue:
        keyList.append(key)

keyList.sort()

chaebin = 0

if len(keyList) > 1:
    chaebin = keyList[1]
else:
    chaebin = keyList[0]

answer.append(chaebin)
answer.append(aList[len(aList)-1] - aList[0])

print(*answer)