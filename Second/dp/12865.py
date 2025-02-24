n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

# 1차원 DP 배열 초기화
dp = [0] * (k+1)

for w, v in items:
    for j in range(k, w-1, -1):
        print("j = == ", j)
        print("dp[j]", dp[j])
        print("dp[j-w]", dp[j-w], v)
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[k])

# 못 풀었음