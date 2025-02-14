str1 = str(input())
str2 = str(input())
n, m = len(str1), len(str2)
answer = 0

dp = [[0] * (m+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        if str1[x-1] == str2[y-1]:
            dp[x][y] = dp[x-1][y-1] + 1
            answer = max(answer, dp[x][y])
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])

print(answer)

