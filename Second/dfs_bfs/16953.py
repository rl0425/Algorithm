from collections import deque

a, b = map(int, input().split())
def bfs():
    q = deque([(a, 1)])
    visited = set([a])
    while q:
        n, cnt = q.popleft()

        if n == b:
            return cnt

        for new_x in [n*2, int(str(n) + str(1))]:
            if new_x <= b and new_x not in visited:
                q.appendleft((new_x, cnt+1))
                visited.add(new_x)
    return -1

print(bfs())