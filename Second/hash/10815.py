import heapq

def dijkstra(start, end):
    q = []
    distance = [float('inf')] * 100001
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if now == end:  # 도착점에 도달하면 종료
            return dist

        if distance[now] < dist:
            continue

        # 순간이동 (0초)
        if now * 2 <= 100000 and distance[now * 2] > dist:
            distance[now * 2] = dist
            heapq.heappush(q, (dist, now * 2))

        # 걷기 (1초)
        for next_pos in [now - 1, now + 1]:
            if 0 <= next_pos <= 100000 and distance[next_pos] > dist + 1:
                distance[next_pos] = dist + 1
                heapq.heappush(q, (dist + 1, next_pos))


n, k = map(int, input().split())
print(dijkstra(n, k))