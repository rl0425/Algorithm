from collections import deque
n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append((n, 0))
    visited = [-1] * 100001
    cnt = [0] * 100001

    visited[n] = 0
    cnt[n] = 1

    while q:
        dest, time = q.popleft()

        for new_x in [dest+1, dest-1, dest*2]:
            if 0 <= new_x <= 100000:
                if visited[new_x] == -1:
                    q.append((new_x, time+1))
                    visited[new_x] = time+1
                    cnt[new_x] = cnt[dest]
                elif visited[new_x] == time+1:
                    cnt[new_x] += cnt[dest]
    return visited[k], cnt[k]

visit, cnt = bfs()

print(visit)
print(cnt)
