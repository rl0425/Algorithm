from collections import deque

a, b = map(int, input().split())

answer = [0 for _ in range(101)]
visited = [False for _ in range(101)]

snake = [0 for _ in range(101)]
climb = [0 for _ in range(101)]

def bfs():
    queue = deque()
    queue.append(1)

    while True:
        num = queue.popleft()

        if num == 100:
            print(answer[100])
            break

        for x in range(1, 7):
            next = num + x
            if next <= 100 and not visited[next]:
                if climb[next] != 0:
                    next = climb[next]

                if snake[next] != 0:
                    next = snake[next]

                if not visited[next]:
                    visited[next] = True
                    answer[next] = answer[num] + 1
                    queue.append(next)

for _ in range(a):
    x, y = map(int, input().split())
    climb[x] = y

for _ in range(b):
    x, y = map(int, input().split())
    snake[x] = y

bfs()