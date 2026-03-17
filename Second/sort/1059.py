s = int(input())
arr = list(map(int, input().split()))
n = int(input())
ans = 0

min = 1
max = 1

arr.sort()


if n in arr:
    print("0")
else:
    for e in arr:
        if e < n:
            min = e+1
        if e > n:
            max = e
        if min and max and max != 1:
            break

    for i in range(min, max):
        for j in range(i+1, max):
            if i <= n and j >= n:
                ans += 1
    print(ans)