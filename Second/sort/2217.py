n = int(input())
arr = []
ans = 0
cnt = 1

for _ in range(n):
    w = int(input())
    arr.append(w)

arr.sort(reverse=True)

for e in arr:
    if ans < cnt * e:
        ans = cnt * e
    cnt += 1

print(ans)
