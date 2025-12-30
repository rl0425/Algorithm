from collections import deque

n = int(input())

def bfs(l, x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0 for _ in range(l)] for _ in range(l)]
    visited[y][x] = 0

    while queue:
        px, py = queue.popleft()
        list = [(1, -2), (2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2)]

        for dx, dy in list:
            if dx + px >= 0 and dx + px < l and dy + py >= 0 and dy + py < l:
                if visited[dy+py][dx+px] > visited[py][px] + 1 or visited[dy+py][dx+px] == 0:
                    visited[dy + py][dx + px] = visited[py][px] + 1
                    queue.append((dx+px, dy+py))

    return visited

for _ in range(n):
    l = int(input())
    x, y = map(int, input().split())
    dx, dy = map(int, input().split())
    if x == dx and y == dy:
        print(0)
    else:
        q = bfs(l, x, y)
        print(q[dy][dx])
