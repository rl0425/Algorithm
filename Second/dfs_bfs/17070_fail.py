# bfs로 풀었더니 3^n 나와서 멸망

from collections import deque

n = int(input())
graph = []

def bfs():
    q = deque()
    q.append([1,0,0,0])
    cnt = 0

    while q:
        x, y, prev_x, prev_y = q.popleft()
        arrow = [(1, 1)]
        if x - prev_x == 1 and y - prev_y == 0:
            arrow.append((1, 0))
        if x - prev_x == 0 and y - prev_y == 1:
            arrow.append((0, 1))
        if x - prev_x == 1 and y - prev_y == 1:
            arrow.append((0, 1))
            arrow.append((1, 0))

        if x == n-1 and y == n-1 :
            cnt += 1
        for dx, dy in arrow:
            new_x, new_y = dx + x, dy + y
            if 0 <= new_x < n and 0 <= new_y < n and graph[new_y][new_x] != 1:
                if dx == 1 and dy == 1:
                    if graph[y][new_x] == 1 or graph[new_y][x] == 1:
                        continue
                q.append([new_x, new_y, x, y])

    return cnt

for _ in range(n):
    graph.append(list(map(int, input().split())))

print(bfs())