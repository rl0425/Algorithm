n = int(input())
cnt = 0
ans = 0

while True:
    if cnt + ans >= n:
        break
    else:
        ans += 1
        cnt += ans

print(ans)