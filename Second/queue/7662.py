import heapq
import sys

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    for _ in range(k):
        s, n = sys.stdin.readline().split()
        if s == "I":
            heapq.heappush(max_heap, -int(n))
            heapq.heappush(min_heap, int(n))
        if s == "D":
            print("max = ", max_heap)
            print("min = ", min_heap)
            if n == '-1':
                print("here")
                if len(max_heap) > 0:
                    heapq.heappop(max_heap)
                elif len(min_heap) > 0:
                    heapq.heappop(min_heap)

            if n == '1':
                if len(min_heap) > 0:
                    heapq.heappop(min_heap)
                elif len(max_heap) > 0:
                    heapq.heappop(max_heap)
            print("max = ", max_heap)
            print("min = ", min_heap)


    if len(max_heap) == 0 and len(min_heap) == 0:
        print("EMPTY")
    elif len(max_heap) != 0 and len(min_heap) != 0:
        print(min_heap[-1], max_heap[-1])
    elif len(max_heap) != 0 and len(min_heap) == 0:
        print(max(max_heap), min(max_heap))
    elif len(max_heap) == 0 and len(min_heap) != 0:
        print(max(min_heap), min(min_heap))