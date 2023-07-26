import heapq

def dijkstra(graph, start):
    # distance = [1e8] * 7
    distance = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    # distance = [1e8] * n
    print("distance= ", distance)

    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        curDistance, curDest = heapq.heappop(queue)

        if distance[curDest] < curDistance:
            continue

        for newDist, newDest in graph[curDest].items():

            print("newDist = ", newDist)
            distances = curDistance + newDist

            if distances < distance[newDest]:
                distance[newDest] = distances
                heapq.heappush(queue, [distances, newDest])



graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
print(dijkstra(graph, 'A'))