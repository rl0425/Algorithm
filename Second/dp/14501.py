n = int(input())
dp = [(0, 0) for _ in range(n)]
maxProfit = 0

for i in range(n):
    t, p = map(int, input().split())
    maxPrev = 0
    if i + t <= n:
        for j in range(i, -1, -1):
            if j + dp[j][0] <= i:
                if maxPrev < dp[j][1]:
                    maxPrev = dp[j][1]
        dp[i] = (t, p + maxPrev)
        if p + maxPrev > maxProfit:
            maxProfit = p + maxPrev
    else:
        dp[i] = (t, maxProfit)

print(maxProfit)