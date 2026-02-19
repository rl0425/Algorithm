x, y = map(int, input().split())
now = (y * 100) // x
ans = -1

start, end = 1, 1000000000

while start <= end:
    mid = (start + end) // 2

    dx, dy = x+mid, y+mid

    sum = ((y + mid) * 100) // (x + mid)

    if sum != now:
        ans = mid
        end = mid - 1

    if sum == now:
        start = mid + 1

print(ans)

