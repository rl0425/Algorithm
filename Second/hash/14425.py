import sys
input = sys.stdin.readline

n, s = map(int, input().split())

mList = {}
sList = []
answer = 0

for _ in range(n):
    e = input().strip()

    if e not in mList:
        mList[e] = 1

for _ in range(s):
    sList.append(input().strip())

sList = list(set(sList))

for e in sList:
    if e in mList:
        answer += 1
        continue

print(answer)