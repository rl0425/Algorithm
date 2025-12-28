import sys
sys.setrecursionlimit(10**7)

def dfs(x, y, arr, visited):
    w = len(arr[y])
    h = len(arr)
    visited[y][x] = True
    rotate = [(0, 1), (0, -1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    for dx, dy in rotate:
        if x + dx < w and y + dy < h and x + dx >= 0 and y + dy >= 0:
            if arr[y+dy][x+dx] == 1 and visited[y+dy][x+dx] == False:
                dfs(x+dx, y+dy, arr, visited)
    return




while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = []

    for i in range(h):
        arr.append(list(map(int, input().split())))

    visited = [[False for _ in range(w)] for _ in range(h)]
    cnt = 0

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 1 and visited[y][x] == False:
                cnt += 1
                dfs(x, y, arr, visited)

    print(cnt)
