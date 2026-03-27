import sys


def solve():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [input().strip() for _ in range(r)]

    queue = set([(0, 0, board[0][0])])
    max_len = 0

    while queue:
        x, y, path = queue.pop()
        max_len = max(max_len, len(path))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < c and 0 <= ny < r:
                if board[ny][nx] not in path:
                    queue.add((nx, ny, path + board[ny][nx]))

    return max_len


print(solve())