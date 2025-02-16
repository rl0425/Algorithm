n = int(input())
m = int(input())

graph = [[float('inf')]*(n+1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for y in range(1,n+1):
    for x in range(1, n+1):
        print(0 if graph[y][x] == float('inf') or y==x else graph[y][x], end=" ")
    print()

