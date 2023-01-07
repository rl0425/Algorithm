a,b = map(int, input().split())

aGon = []
bGon = []

aMax = []
bMax = []

answer = []

for x in range(1, a+1):
    if a % x == 0:
        aGon.append(x)

for x in range(1, b+1):
    if b % x == 0:
        bGon.append(x)

for x in range(len(aGon)-1,0,-1):
    if aGon[x] in bGon:
        answer.append(aGon[x])
        break

if len(answer) == 0:
    answer.append(1)

maxGong = a*b

count = 1
while True:
    if a * count >= maxGong:
        break
    else:
        aMax.append(a*count)
        count += 1

count = 1
while True:
    if b * count >= maxGong:
        break
    else:
        bMax.append(b*count)
        count += 1

for x in aMax:
    if x in bMax:
        answer.append(x)
        break

if len(answer) == 1:
    answer.append(maxGong)

print(*answer)
