import sys
sys.setrecursionlimit(10**7)

n = int(input())
arr = []
ans = 0

dp = [[0, 0, 0] for _ in range(n)]

for _ in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    if i == 0:
        dp[i][0] = arr[i]
        dp[i][1] = arr[i]
        dp[i][2] = arr[i]
    elif i == 1:
        dp[i][0] = arr[i]
        dp[i][1] = arr[i]
        dp[i][2] = dp[i-1][0] + arr[i]
    elif i == 2:
        dp[i][0] = arr[i]
        dp[i][1] = dp[i-2][0] + arr[i]
        dp[i][2] = dp[i-1][0] + arr[i]
    else:
        dp[i][0] = max(dp[i-3][0], dp[i-3][1], dp[i-3][2]) + arr[i]
        dp[i][1] = max(dp[i-2][0], dp[i-2][1], dp[i-2][2]) + arr[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + arr[i]

    if ans < dp[i][0]:
        ans = dp[i][0]
    if ans < dp[i][1]:
        ans = dp[i][1]
    if ans < dp[i][2]:
        ans = dp[i][2]

print(ans)