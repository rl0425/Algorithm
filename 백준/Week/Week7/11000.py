import heapq
import sys
input = sys.stdin.readline

n = int(input())

list = [list(map(int, input().split())) for i in range(n)]
list.sort()

queue = []
heapq.heappush(queue, list[0][1])

for i in range(1, n):
    if list[i][0] < queue[0]:
        heapq.heappush(queue, list[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, list[i][1])

print(len(queue))