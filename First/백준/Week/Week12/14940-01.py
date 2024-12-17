import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
inputList = [0 for _ in range(a)]
visited = [[False for _ in range(b)] for _ in range(a)]

def func(list):
    for x in range(a):
        for y in range(b):
            if list[x][y] == 2:
                queue = deque()
                queue.append((x,y))
                visited[x][y] = True
                list[x][y] = 0

                dx = [-1,1,0,0]
                dy = [0,0,-1,1]

                while queue:
                    newX, newY = queue.popleft()

                    for e in range(4):
                        nx = newX + dx[e]
                        ny = newY + dy[e]

                        if nx < 0 or nx >= a or ny < 0 or ny >= b:
                            continue
                        elif list[nx][ny] == 0:
                            visited[nx][ny] = True
                            continue
                        elif list[nx][ny] == 1 and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            list[nx][ny] = list[newX][newY] + 1

                return;

for x in range(a):
    inputList[x] = list(map(int, input().split()))

func(inputList)

for x in range(a):
    for y in range(b):
        if visited[x][y] == False and inputList[x][y] != 0:
            inputList[x][y] = -1

for x in range(a):
    print(*inputList[x])

