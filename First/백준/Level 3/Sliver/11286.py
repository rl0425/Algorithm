import heapq

heap_q = []

a = int(input())

for x in range(a):
    num = int(input())

    if num != 0:
        heapq.heappush(heap_q, abs(num))

    else:
        if heap_q:
            print(heapq.heappop(heap_q))
        else:
            print(-1)