from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
info = [[] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
start = [-1, -1]
answer = 0

def bfs(startX, startY):
    global answer

    queue = deque()
    queue.append((startX, startY))
    while queue:
        x, y = queue.popleft()

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            # if 0 <= nx < n and 0 <= ny < m and info[nx][ny] != 'X' and not visited[nx][ny]:
            #     visited[nx][ny] = True
            #     queue.append([nx, ny])
            #
            #     if info[nx][ny] == 'P':
            #         answer += 1

            if nX < 0 or nX >= n or nY < 0 or nY >= m:
                continue

            if info[nX][nY] != "X" and not visited[nX][nY]:
                if info[nX][nY] == "P":
                    answer += 1
                    visited[nX][nY] = True
                    queue.append((nX, nY))

                if info[nX][nY] == "O":
                    visited[nX][nY] = True
                    queue.append((nX, nY))


for i in range(n):
    info[i] = [*input()]
    for j in range(m):
        if info[i][j] == 'I':
            start[0], start[1] = i, j

bfs(start[0], start[1])

if answer == 0:
    print("TT")
else:
    print(answer)