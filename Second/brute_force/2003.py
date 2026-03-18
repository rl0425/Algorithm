n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


for i in range(len(arr)-1, -1, -1):
    sum = arr[i]
    if sum == m:
        ans += 1
        continue
    if sum > m:
        continue
    for j in range(i-1, -1, -1):
        sum += arr[j]
        if sum == m:
            ans += 1
            break
        if sum > m:
            break
print(ans)