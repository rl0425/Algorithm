import heapq
import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline


def dijkstra(start, graph, n):
    # 1. 거리 테이블을 무한대로 초기화
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    # 2. 우선순위 큐 생성 (거리, 노드) 저장
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # 이미 처리된 노드라면 패스
        if distances[current_node] < current_dist:
            continue

        # 인접 노드 확인
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # 더 짧은 경로를 찾았다면 업데이트 후 큐에 삽입
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# 입력 처리
n, m, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]  # 정방향 (X -> 집)
rev_adj = [[] for _ in range(n + 1)]  # 역방향 (집 -> X)

for _ in range(m):
    u, v, t = map(int, input().split())
    adj[u].append((v, t))
    rev_adj[v].append((u, t))

# 3. 딱 두 번만 실행!
dist_to_home = dijkstra(x, adj, n)  # X번 마을에서 각 집으로 돌아오는 최단 시간
dist_to_party = dijkstra(x, rev_adj, n)  # 각 집에서 X번 마을로 가는 최단 시간

# 4. 왕복 시간 중 최댓값 찾기
max_time = 0
for i in range(1, n + 1):
    max_time = max(max_time, dist_to_home[i] + dist_to_party[i])

print(max_time)