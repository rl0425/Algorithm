n = int(input())
nlist = list(map(int, input().split()))
sum = int(input())

maxN = max(nlist)
arr = [0 for _ in range(2000001)]

ans = 0

for e in nlist:
    arr[e] = 1

for e in nlist:
    if arr[e] == 1:
        if sum - e > 0 and arr[sum - e] >= 1 and e != sum - e:
            ans += 1
            arr[e] = 0
            arr[sum - e] = 0

print(ans)