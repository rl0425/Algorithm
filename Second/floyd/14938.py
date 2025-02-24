n, m, r = map(int, input().split())
arr = list(map(int, input().split()))

graph = [[16] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
answer = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m or i == j:
            temp += arr[j-1]
    answer = max(temp, answer)
print(answer)
