n, m = map(int, input().split())
arr = []
max = 1

for _ in range(n):
    arr.append(list(map(str, input())))

for y in range(n):
    for x in range(m):
        cnt = 0
        while True:
            cnt += 1
            if y + cnt >= n:
                break
            if x + cnt >= m:
                break
            if arr[y][x] == arr[y+cnt][x] == arr[y][x+cnt] == arr[y+cnt][x+cnt]:
                if (cnt+1) ** 2 > max:
                    max = (cnt+1) ** 2

print(max)

