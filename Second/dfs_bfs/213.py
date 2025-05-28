def find_largest_shape(grid):
    n, m = len(grid), len(grid[0])
    max_area = 0

    # 모든 격자 위치 탐색
    for i in range(n):
        for j in range(m):
            for height in range(2, n + 1):  # 세로 길이 (최소 2)
                if i + height > n:
                    continue

                for width in range(3, m + 1):  # 가로 길이 (최소 3)
                    if j + width > m:
                        continue

                    # 현재 위치의 소유자
                    owner = grid[i][j]

                    # 1. ㄷ자 모양 (위쪽과 양옆)
                    if check_top_shape(grid, i, j, height, width, owner):
                        area = width + 2 * (height - 1)
                        max_area = max(max_area, area)

                    # 2. U자 모양 (아래쪽과 양옆)
                    if check_bottom_shape(grid, i, j, height, width, owner):
                        area = width + 2 * (height - 1)
                        max_area = max(max_area, area)

                    # 3. 왼쪽 ㄱ자 모양 (왼쪽과 위아래)
                    if check_left_shape(grid, i, j, height, width, owner):
                        area = height + 2 * (width - 1)
                        max_area = max(max_area, area)

                    # 4. 오른쪽 ㄱ자 모양 (오른쪽과 위아래)
                    if check_right_shape(grid, i, j, height, width, owner):
                        area = height + 2 * (width - 1)
                        max_area = max(max_area, area)

    return max_area


# ㄷ자 모양 (위쪽과 양옆)
def check_top_shape(grid, i, j, height, width, owner):
    n, m = len(grid), len(grid[0])

    # 위쪽 가로줄 확인
    for k in range(width):
        if j + k >= m or grid[i][j + k] != owner:
            return False

    # 왼쪽 세로줄 확인
    for k in range(1, height):
        if i + k >= n or grid[i + k][j] != owner:
            return False

    # 오른쪽 세로줄 확인
    for k in range(1, height):
        if i + k >= n or grid[i + k][j + width - 1] != owner:
            return False

    return True


# U자 모양 (아래쪽과 양옆)
def check_bottom_shape(grid, i, j, height, width, owner):
    n, m = len(grid), len(grid[0])

    # 아래쪽 가로줄 확인
    for k in range(width):
        if j + k >= m or grid[i + height - 1][j + k] != owner:
            return False

    # 왼쪽 세로줄 확인
    for k in range(height - 1):
        if i + k >= n or grid[i + k][j] != owner:
            return False

    # 오른쪽 세로줄 확인
    for k in range(height - 1):
        if i + k >= n or grid[i + k][j + width - 1] != owner:
            return False

    return True


# 왼쪽 ㄱ자 모양 (왼쪽과 위아래)
def check_left_shape(grid, i, j, height, width, owner):
    n, m = len(grid), len(grid[0])

    # 왼쪽 세로줄 확인
    for k in range(height):
        if i + k >= n or grid[i + k][j] != owner:
            return False

    # 위쪽 가로줄 확인
    for k in range(1, width):
        if j + k >= m or grid[i][j + k] != owner:
            return False

    # 아래쪽 가로줄 확인
    for k in range(1, width):
        if j + k >= m or grid[i + height - 1][j + k] != owner:
            return False

    return True


# 오른쪽 ㄱ자 모양 (오른쪽과 위아래)
def check_right_shape(grid, i, j, height, width, owner):
    n, m = len(grid), len(grid[0])

    # 오른쪽 세로줄 확인
    for k in range(height):
        if i + k >= n or j + width - 1 >= m or grid[i + k][j + width - 1] != owner:
            return False

    # 위쪽 가로줄 확인
    for k in range(width - 1):
        if j + k >= m or grid[i][j + k] != owner:
            return False

    # 아래쪽 가로줄 확인
    for k in range(width - 1):
        if j + k >= m or grid[i + height - 1][j + k] != owner:
            return False

    return True


# 입력 처리 함수
def main():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))

    result = find_largest_shape(grid)
    print(result)


# 예시 실행
if __name__ == "__main__":
    # 예시 격자들
    test_grids = [
        # 모두 A인 격자
        [
            ['A', 'A', 'A'],
            ['A', 'A', 'A'],
            ['A', 'A', 'A'],
            ['A', 'A', 'A']
        ],
        # ㄷ자 모양 격자
        [
            ['A', 'A', 'A'],
            ['A', 'B', 'A'],
            ['B', 'B', 'B']
        ],
        # U자 모양 격자
        [
            ['A', 'B', 'A'],
            ['A', 'B', 'A'],
            ['A', 'A', 'A']
        ],
        # 왼쪽 ㄱ자 모양 격자
        [
            ['A', 'A', 'A'],
            ['A', 'B', 'B'],
            ['A', 'A', 'A']
        ],
        # 오른쪽 ㄱ자 모양 격자
        [
            ['A', 'A', 'A'],
            ['B', 'B', 'A'],
            ['A', 'A', 'A']
        ]
    ]

    for idx, grid in enumerate(test_grids):
        print(f"예시 {idx + 1} 최대 넓이:", find_largest_shape(grid))