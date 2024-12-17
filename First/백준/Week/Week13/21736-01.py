from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]
numArr = [[] for _ in range(n)]
start = [-1, -1]

def bfs():
    queue = deque()
    queue.append([start[0], start[1]])
    visited[start[0]][start[1]] = True

    answer = 0

    while queue:
        x, y = queue.popleft()

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < n and 0 <= ny < m and numArr[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])

                if numArr[nx][ny] == 'P':
                    answer += 1

    return ['TT', answer] [answer > 0]

for i in range(n):
    numArr[i] = [*input()]
    for j in range(m):
        if numArr[i][j] == 'I':
            start[0], start[1] = i, j

print(bfs())