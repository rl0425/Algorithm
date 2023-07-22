n = int(input())

tree = {}

def dfs(root, dist):
    for x in tree[root]:
        if distance[x[0]] == -1 and x[0] != 0:
            distance[x[0]] = dist + x[1]
            dfs(x[0], dist + x[1])

for _ in range(n-1):
    s, e, d = map(int, input().split())

    if s not in tree:
        tree[s] = [(e,d)]
    else:
        tree[s].append((e,d))

    if e not in tree:
        tree[e] = [(s,d)]
    else:
        tree[e].append((s,d))

if n == 1:
    print(0)

else:
    distance = [-1] * (n+1)
    distance[1] = 0
    dfs(1, 0)

    maxIdx = distance.index(max(distance))
    distance = [-1] * (n+1)
    distance[maxIdx] = 0

    dfs(maxIdx, 0)

    print(max(distance))
