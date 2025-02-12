from collections import deque

n = int(input())
arrZone = []
maxArrHeight = 1
maxAreaZone = 0

def maze_dfs(arr, waterLevel):
    visited = set()
    island = 0
    def dfs(arr, start):
        queue = deque()

        x, y = start[0], start[1]
        location = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for dx, dy in location:
                new_x, new_y = dx + x, dy + y
                if (new_x, new_y) not in visited and new_x >= 0 and new_y >= 0 and new_x <= len(arr)-1 and new_y <= len(arr)-1:
                    if arr[new_x][new_y] > waterLevel:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
        return True

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > waterLevel and (i, j) not in visited:
                dfs(arr, (i, j))
                island += 1
    return island

for _ in range(n):
    arr = list(map(int, input().split()))
    tempMax = max(arr)
    if tempMax > maxArrHeight:
        maxArrHeight = tempMax
    arrZone.append(arr)

for i in range(0, maxArrHeight):
    isLandNum = maze_dfs(arrZone, i)
    if isLandNum > maxAreaZone:
        maxAreaZone = isLandNum

print(maxAreaZone)

# dfs 이해 안되서 걍 BFS로 품.