from collections import deque
import copy

n, m = map(int, input().split())
path = []
answer = -1

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1

    arrow = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while queue:
        py, px = queue.popleft()

        for dx, dy in arrow:
            nx, ny = px + dx, py + dy

            # visited[x][y]를 visited[ny][nx]로 수정
            if 0 <= nx < m and 0 <= ny < n and path[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[py][px] + 1
                queue.append((ny, nx))
    return visited

def re_bfs(x, y, visited):
    queue = deque()
    queue.append((y, x))
    arrow = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    min_arr = []

    for dx, dy in arrow:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] != -1:
            min_arr.append(visited[ny][nx])

    if len(min_arr) == 0:
        return -1
    min_value = min(min_arr)
    visited[y][x] = min(min_arr) + 1

    while queue:
        py, px = queue.popleft()
        for dx, dy in arrow:
            nx, ny = px + dx, py + dy

            if 0 <= nx < m and 0 <= ny < n and path[ny][nx] == 0:
                if (visited[ny][nx] > visited[py][px] + 1) or visited[ny][nx] == -1:
                    visited[ny][nx] = visited[py][px] + 1
                    queue.append((ny, nx))
    return visited[-1][-1]

for _ in range(n):
    path.append(list(map(int, list(input()))))

visited = bfs(0, 0)

for y in range(n-1):
    for x in range(m-1):
        if visited[y][x] == -1:
            temp_visited = copy.deepcopy(visited)
            min_value = re_bfs(x, y, temp_visited)

            if min_value != -1:
                if answer == -1:
                    answer = min_value
                else:
                    answer = min(answer, min_value)

print(answer)
