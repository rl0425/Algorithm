def check(k):  # k : 놓은 말 개수
    global n, cnt

    if k == n:
        cnt += 1
        return

    for i in range(n):
        if col[i] == 0 and up[k + i] == 0 and down[(n - 1) + k - i] == 0:
            col[i] = 1
            up[k + i] = 1
            down[(n - 1) + k - i] = 1
            check(k + 1) # 다음 queen 확인
            # 잘못 놓았을 경우 되돌려놓기
            col[i] = 0
            up[k + i] = 0
            down[(n - 1) + k - i] = 0


import sys

n = int(sys.stdin.readline())
c = [[0] * n for _ in range(n)]

# 열 저장
col = [0] * n

# y = x 대각선 저장
up = [0] * (2 * (n - 1) + 1)

# y = -x 대각선 저장
down = [0] * (2 * (n - 1) + 1)

cnt = 0

check(0)
print(cnt)