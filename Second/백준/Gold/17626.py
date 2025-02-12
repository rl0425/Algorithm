n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    min_value = 4
    j = 1
    while j*j <= i:
        min_value = min(min_value, dp[i - j * j])
        j += 1
    dp[i] = min_value + 1

print(dp[n])