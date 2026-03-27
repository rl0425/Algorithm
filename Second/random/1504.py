import heapq
import sys
input = sys.stdin.readline

n, e = map(int,input().split())
graph = {}

def Dij(start, end, graph):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        r, v = heapq.heappop(q)
        if v not in graph:
            continue

        if dist[v] < r:
            continue
        for nowR, nowV in graph[v]:
            # print("nowR = ", nowR, nowV)
            newD = r + nowR

            if newD < dist[nowV]:
                dist[nowV] = newD
                heapq.heappush(q, (newD, nowV))
    return dist[end]

for _ in range(e):
    x, y, z = map(int, input().split())

    if x in graph:
        graph[x].append((z, y))
    else:
        graph[x] = [(z, y)]

    if y in graph:
        graph[y].append((z, x))
    else:
        graph[y] = [(z, x)]
v1, v2 = map(int, input().split())
if graph:
    # print("Dij(1, v1, graph) + Dij(v1, v2, graph) + Dij(v2, n, graph) = ", Dij(1, v1, graph) + Dij(v1, v2, graph) + Dij(v2, n, graph))
    # print("Dij(1, v2, graph) + Dij(v2, v1, graph) + Dij(v1, n, graph) = ", Dij(1, v2, graph) + Dij(v2, v1, graph) + Dij(v1, n, graph))
    ans = min((Dij(1, v1, graph) + Dij(v1, v2, graph) + Dij(v2, n, graph)), (Dij(1, v2, graph) + Dij(v2, v1, graph) + Dij(v1, n, graph)))
    print(ans if ans != float('inf') else -1)
else:
    print('-1')

