def maze_dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

    def dfs(x, y):
        if (x, y) == end:
            return True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상

        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if (next_x, next_y) not in visited and is_valid(next_x, next_y):
                visited.add((next_x, next_y))
                path.append((next_x, next_y))
                if dfs(next_x, next_y):
                    return True
                path.pop()
        return False

    visited.add(start)
    path.append(start)
    dfs(start[0], start[1])
    return path


# 미로 예시 (0: 길, 1: 벽)
maze = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

start = (0, 0)
end = (3, 3)
path = maze_dfs(maze, start, end)
print("\n\n미로 경로:", path)
