import heapq, sys
input = sys.stdin.readline

a = int(input())
heap = []

for x in range(a):
    data = int(input())

    if data == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-data, data))
