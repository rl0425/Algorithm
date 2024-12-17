import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue:
        n_di, n_de = heapq.heappop(queue)

        print("n_de = ", n_de)
        print("n_de = ", graph[n_de])


        if dist[n_de] < n_di:
            continue;

        for c_de, c_di in graph[n_de].items():

            n_distance = n_di + c_di

            if n_distance < dist[c_de]:
                dist[c_de] = n_distance
                heapq.heappush(queue, [n_distance, c_de])
    return dist

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
print(dijkstra(graph, 'A'))