from collections import deque

n = int(input())
m1, m2 = map(int, input().split())
r = int(input())

dict = {}
visited = [-1 for _ in range(n+1)]
par = {}

def bfs(num):
    queue = deque()
    ans = -1

    if num in par:
        queue.append((par[num], 1))
        visited[par[num]] = 1

    if num in dict:
        for e in dict[num]:
            queue.append((e, 1))
            visited[int(e)] = 1

    while queue:
        dn, cnt = queue.popleft()
        if dn == m2:
            ans = cnt
            break
        else:
            if dn in par and visited[int(par[dn])] == -1:
                queue.append((par[dn], cnt+1))
                visited[int(par[dn])] = 1

            if dn in dict:
                for e in dict[dn]:
                    if visited[int(e)] == -1:
                        queue.append((e, cnt+1))
                        visited[int(e)] = 1

    return ans

for _ in range(r):
    x, y = map(int, input().split())
    if x in dict:
        dict[x].append(y)
    else:
        dict[x] = [y]
    par[y] = x

print(bfs(m1))