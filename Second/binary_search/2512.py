n = int(input())
nList = list(map(int, input().split()))
maxCnt = int(input())
res = 0

start, end = 0, max(nList)

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for e in nList:
        if e <= mid:
            sum += e
        if e > mid:
            sum += mid

    if sum <= maxCnt:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)