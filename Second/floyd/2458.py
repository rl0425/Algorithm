n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[k][j] and graph[i][k]:
                graph[i][j] = 1

for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if graph[i][j] or graph[j][i]:
            sum += 1
    if sum == n-1:
        ans += 1

print(ans)

