from collections import deque

m, n, k = map(int,input().split())
graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
answer = []

def bfs(x, y):
    if visited[y][x] or graph[y][x] == 1:
        return 0
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    arrow = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cnt = 1

    while q:
        x, y = q.popleft()

        for dx, dy in arrow:
            new_x, new_y = dx+x, dy+y
            if 0 <= new_x < n and 0 <= new_y < m and not visited[new_y][new_x] and graph[new_y][new_x] != 1:
                q.append((new_x, new_y))
                visited[new_y][new_x] = True
                cnt += 1
    return cnt

for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    for x in range(x0, x1):
        for y in range(y0, y1):
            graph[y][x] = 1

for y in range(m):
    for x in range(n):
        ans = bfs(x, y)
        if ans != 0:
            answer.append(ans)

answer.sort()
print(len(answer))
print(*answer)