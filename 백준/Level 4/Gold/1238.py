import heapq

a,b,c = map(int, input().split())
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

graph = {}

for x in range(b):
    d, e, f = map(int, input().split())

    if d not in graph:
        graph[d] = {e: f}
    else:
        graph[d][e] = f

max = 0
destination = dijkstra(graph, c)

for x in range(1, a+1):
    if x != c:
        result = dijkstra(graph, x)
        if result[c] + destination[x] > max:
            max = result[c] + destination[x]

print(max)
