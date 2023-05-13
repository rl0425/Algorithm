import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())

depth = [300000]*(n+1)
heap = []
graph = [[] for _ in range(n + 1)]

for i in range(m):
    c, d, e = map(int, input().split())
    graph[c].append((e, d))

def dijkstra(start):
    depth[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        now_distance, now_location = heapq.heappop(heap)

        if depth[now_location] < now_distance:
            continue

        for nex_distance, next_location in graph[now_location]:
            next_distance = nex_distance + now_distance
            if next_distance < depth[next_location]:
                depth[next_location] = next_distance
                heapq.heappush(heap, (depth[next_location], next_location))

dijkstra(start)

for i in range(1, n+1):
    if depth[i] == 300000:
        print("INF")
    else:
        print(depth[i])

# for x in range(m):
#     c, d, e = map(int,input().split())
#
#     if c not in graph:
#         graph[c] = {d: e}
#     else:
#         graph[c][d] = e
#
#     if d not in graph:
#         graph[d] = {c: e}
#     else:
#         graph[d][c] = e
#
# def dijkstra(start):
#     distances = {node: float('inf') for node in range(1,n+1)}  # start로 부터의 거리 값을 저장하기 위함
#     distances[start] = 0  # 시작 값은 0이어야 함
#     queue = []
#     heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.
#
#     print("distances= ", distances)
#
#     while queue:  # queue에 남아 있는 노드가 없으면 끝
#         current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
#
#         if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
#             continue
#
#         for new_destination, new_distance in graph[current_destination].items():
#             distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
#             print("new_destination= ", new_destination)
#             if new_destination in distances:
#                 if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
#                     distances[new_destination] = distance
#                     heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
#
#     return distances

#초기화