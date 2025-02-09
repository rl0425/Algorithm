from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]  # 한 번만 생성
    oil_size = [0] * m  # 각 열의 크기를 저장할 배열

    def bfs(start_x, start_y):
        size = 1  # 현재 덩어리의 크기
        q = deque([(start_x, start_y)])
        cols = {start_y}  # 이 덩어리가 영향을 주는 열들
        visited[start_x][start_y] = True

        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cols.add(ny)  # 새로운 열 추가
                    size += 1

        # 이 덩어리가 영향을 주는 모든 열에 크기를 더함
        for col in cols:
            print("col= ", col)
            oil_size[col] += size

    # 모든 위치를 한 번씩만 확인
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                bfs(i, j)  # 각 덩어리는 딱 한 번만 계산

    print("max = ", max(oil_size))
    return max(oil_size)
land = 	[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
solution(land)