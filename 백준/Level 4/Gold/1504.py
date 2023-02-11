import heapq
import sys
input = sys.stdin.readline

a,b = map(int, input().split())
graph = {}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, a+1)}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        startDistnace, startPoint = heapq.heappop(queue)

        if distances[startPoint] < startDistnace:
            continue
        elif startPoint in graph:
            for newPoint, newDistance in graph[startPoint].items():
                distance = startDistnace + newDistance

                if distances[newPoint] > distance:
                    distances[newPoint] = distance
                    heapq.heappush(queue, [distance, newPoint])

    return distances


for x in range(b):
    c, d, e = map(int,input().split())

    if c not in graph:
        graph[c] = {d:e}
    else:
        graph[c][d] = e

    if d not in graph:
        graph[d] = {c:e}
    else:
        graph[d][c] = e

f, g = map(int, input().split())

start = dijkstra(graph, 1)
first = dijkstra(graph, f)
second = dijkstra(graph, g)

fMethod = start[f] + first[g] + second[a]
SMethod = start[g] + second[f] + first[a]

if SMethod > 100000000000 and fMethod > 100000000000:
    print(-1)
elif fMethod > SMethod:
    print(SMethod)
else:
    print(fMethod)