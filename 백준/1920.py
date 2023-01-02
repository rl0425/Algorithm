a = int(input())
aList = list(map(int, input().split()))
b = int(input())
bList = list(map(int, input().split()))

aSet = set(aList)

answer = []

for x in bList:
    if x in aSet:
        answer.append("1")
    else:
        answer.append("0")

print(*answer)