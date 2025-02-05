import heapq

q = []
INF = 2e8

def dijkstra(case):
    q = []
    distance = [[INF] * len(case) for _ in range(len(case))]
    heapq.heappush(q, (0, 0, case[0][0]))
    while q:
        x, y, dist = heapq.heappop(q)

        if distance[x][y] < dist:
            continue;

        if y < len(case)-1:
            rightCost = case[x][y+1] + dist
            if rightCost < distance[x][y+1]:
                distance[x][y+1] = rightCost
                heapq.heappush(q, (x, y+1, rightCost))
        if x < len(case)-1:
            bottomCost = case[x+1][y] + dist
            if bottomCost < distance[x+1][y]:
                distance[x+1][y] = bottomCost
                heapq.heappush(q, (x+1, y, bottomCost))
        if x > 0:
            leftCost = case[x-1][y] + dist
            if leftCost < distance[x-1][y]:
                distance[x-1][y] = leftCost
                heapq.heappush(q, (x-1, y, leftCost))
        if y > 0:
            topCost = case[x][y-1] + dist
            if topCost < distance[x][y-1]:
                distance[x][y-1] = topCost
                heapq.heappush(q, (x, y-1, topCost))
        if x == len(case)-1 and y == len(case)-1:
            distance[x][y] = dist
    return distance[x][y]

while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for x in range(n):
        arr.append(list(map(int, input().split())))
    q.append(arr)

for i in range(len(q)):
    print(f"Problem {i+1}: {dijkstra(q[i])}")

# 1try, solving time : 1hour under