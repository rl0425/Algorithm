n = int(input())
nList = list(map(int, input().split()))
arr = []

for i in range(len(nList)):
    arr.append((nList[i], i))

sArr = sorted(arr)

P = [0] * n

for i in range(len(sArr)):
    val, origin = sArr[i]

    P[origin] = i

print(*P)
