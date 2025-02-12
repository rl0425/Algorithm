n = int(input())
q_arr = []
dp = [0] * 31
dp[0] = 1
dp[1] = 1

for _ in range(n):
    q_arr.append(list(map(int, input().split())))

for i in range(2, 31):
    dp[i] = i * dp[i-1]

for q in q_arr:
    answer = dp[q[1]]/(dp[q[1] - q[0]] * dp[q[0]])
    print(int(answer))