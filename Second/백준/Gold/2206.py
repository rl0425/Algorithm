from collections import deque

n, m = map(int, input().split())
path = []

def bfs():
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    arrow = [(1,0), (0, 1), (-1, 0), (0, -1)]
    while q:
        px, py, broken = q.popleft()

        if px == m-1 and py == n-1:
            return visited[py][px][broken]

        for dx, dy in arrow:
            new_x, new_y = px+dx, py+dy
            if 0 <= new_x < m and 0 <= new_y < n:
                if path[new_y][new_x] == 1 and broken == 0:
                    visited[new_y][new_x][1] = visited[py][px][0] + 1
                    q.append((new_x, new_y, 1))
                elif path[new_y][new_x] == 0 and visited[new_y][new_x][broken] == 0:
                    visited[new_y][new_x][broken] = visited[py][px][broken] + 1
                    q.append((new_x, new_y, broken))
    return -1

for _ in range(n):
    path.append(list(map(int, list(input()))))

print(bfs())