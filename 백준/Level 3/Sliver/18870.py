a = int(input())
b = list(map(int, input().split()))

dictSet = {}
answer = []
count = 0

c = list(b)
b.sort()
for x in b:
    if x not in dictSet:
        dictSet[x] = count
        count += 1

for x in c:
    answer.append(dictSet[x])

print(*answer)


