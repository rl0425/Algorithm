import heapq

n, m = 4, 5
k = 1
INF = 1e8

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)
print(distance)

'''
1 2 3
1 3 5
2 3 2
2 4 6
3 2 1
3 4 4
'''

