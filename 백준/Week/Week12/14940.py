import sys
from collections import deque

input = sys.stdin.readline

a,b = map(int,input().split())

inputList = [0 for _ in range(a)]
visited = [[False for _ in range(b)] for _ in range(a)]
answerList = [[0 for _ in range(a)] for _ in range(b)]

goal = ""
def func(list,x,y):
    queue = deque()

    # print("x, y = ", x,y)

    if list[x][y] == 0:
        return 0;

    if x == goal[0] and y == goal[1]:
        return 0;

    if x - 1 >= 0 and list[x - 1][y] != 0:

        if x-1 == goal[0] and y == goal[1]:
            return 1
        queue.append((int(x-1), int(y)))
    if x + 1 < a and list[x + 1][y] != 0:

        if x+1 == goal[0] and y == goal[1]:
            return 1
        queue.append((int(x+1), int(y)))
    if y - 1 >= 0 and list[x][y - 1] != 0:

        if x == goal[0] and y-1 == goal[1]:
            return 1
        queue.append((int(x), int(y-1)))
    if y + 1 < b and list[x][y + 1] != 0:

        if x == goal[0] and y+1 == goal[1]:
            return 1
        queue.append((int(x), int(y+1)))

    return recursive(list, queue, 1)

def recursive(list, queue, count):
    newQueue = deque()
    stop = False
    global goal

    if len(queue) == 0:
        return -1

    while len(queue):
        newX, newY = queue.popleft()
        # print("n = ", newX, newY)

        if newX - 1 >= 0 and list[newX - 1][newY] != 0:
            # print("11")

            if newX - 1 == goal[0] and newY == goal[1]:
                stop = True

            if visited[newX -1][newY] == False:
                newQueue.append((newX - 1, newY))
                visited[newX - 1][newY] = True

        if newX + 1 < a and list[newX + 1][newY] != 0:
            # print("22")

            if newX + 1 == goal[0] and newY == goal[1]:
                stop = True

            if visited[newX +1][newY] == False:
                newQueue.append((newX + 1, newY))
                visited[newX + 1][newY] = True
        if newY - 1 >= 0 and list[newX][newY - 1] != 0:
            # print("33")

            if newX == goal[0] and newY - 1 == goal[1]:
                stop = True

            if visited[newX][newY-1] == False:
                newQueue.append((newX, newY - 1))
                visited[newX][newY-1] = True
        if newY + 1 < b and list[newX][newY + 1] != 0:
            # print("44")

            if newX == goal[0] and newY + 1 == goal[1]:
                stop = True
            if visited[newX][newY+1] == False:
                newQueue.append((newX, newY + 1))
                visited[newX][newY+1] = True

        if stop:
            break;

    if stop:
        # print("count = ", count)
        return count + 1
    else:
        return recursive(list, newQueue, count+1)

for x in range(a):
    inputList[x] = list(map(int, input().split()))

for x in range(a):
    for y in range(b):
        if inputList[x][y] == 2:
            goal = [int(x), int(y)]

for x in range(a):
    for y in range(b):
        answerList[x][y] = func(inputList,x,y)
        visited = [[False for _ in range(b)] for _ in range(a)]
        # print("################################################################answerList[x][y] = ", answerList[x][y])

for x in range(a):
    print(*answerList[x])

