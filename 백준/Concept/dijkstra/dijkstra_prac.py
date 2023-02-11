import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        startD, startP = heapq.heappop(queue)

        if distances[startP] < startD:
            continue

        for nextP, nextD in graph[startP].items():
            distance = startD + nextD
            if distance < distances[nextP]:
                distances[nextP] = distance
                heapq.heappush(queue, [distance, nextP])

    return distances


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
print(dijkstra(graph, 'A'))