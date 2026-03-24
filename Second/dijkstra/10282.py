import sys
import heapq
input = sys.stdin.readline

n = int(input())

def dijkstra(start, graph, m):
    queue = []
    dist = [float('inf') for _ in range(m+1)]
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        time, now = heapq.heappop(queue)

        if time > dist[now]:
            continue
        for next, n_time in graph[now]:
            cost = time + n_time

            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(queue, (cost, next))

    maxNum = max([x for x in dist if x != float('inf')], default=0)
    length = len([x for x in dist if x != float('inf')])

    print(length, maxNum)

for _ in range(n):
    m, d, c = map(int, input().split())
    graph = [[] for _ in range(m+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    gr = dijkstra(c, graph, m)


