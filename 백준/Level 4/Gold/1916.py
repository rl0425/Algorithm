import heapq, sys
input = sys.stdin.readline

n = int(input())
m = int(input())

busSet = {}
def dijkstra(busSet, start):
    # 거리를 저장할 배열생성
    distArr = {node: float('inf') for node in range(n + 1)}
    # 자기 자신의 거리 0
    distArr[start] = 0

    queue = []
    heapq.heappush(queue, [distArr[start], start])

    while queue:
        now_distance, now_destination = heapq.heappop(queue)

        # 배열목록에 목적지에 해당하는 버스가 없거나 저장된 거리보다 현재의 거리가 더 클때는 생략
        if now_destination not in busSet or distArr[now_destination] < now_distance:
            continue
        for new_destination, new_distance in busSet[now_destination].items():
            # 여기까지 온 거리 + 현재 버스의 거리들을 더하기
            distance = now_distance + new_distance

            # 기존 거리가 더 크면
            if distance < distArr[new_destination]:
                # 기존 거리 갱신
                distArr[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distArr

# dict 만들어주기
for x in range(m):
    s, e, d = map(int, input().split())

    if s in busSet:
        if e in busSet[s]:
            if busSet[s][e] > d:
                busSet[s][e] = d
        else:
            busSet[s][e] = d
    else:
        busSet[s] = {e: d}

start, destination = map(int, input().split())
print(dijkstra(busSet, start)[destination])
