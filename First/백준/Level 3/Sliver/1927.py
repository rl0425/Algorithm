import sys, heapq
input = sys.stdin.readline


heap = []

a = int(input())

for x in range(a):
    enter = int(input())

    if enter != 0:
        heapq.heappush(heap, enter)

    else:
        if len(heap) == 0:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result)



