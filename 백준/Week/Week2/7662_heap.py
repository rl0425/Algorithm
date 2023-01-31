from heapq import heappush, heappop

numInput = int(input())

maxNum = "A"
minNum = "B"

for number in range(numInput):
    num = int(input())
    heap = []

    for x in range(num):
        a, b = input().split()

        if a == "I":
            heappush(heap, (0-int(b), b))
        elif a == "D":
            if b == str(1):
                if len(heap) > 0:
                    heappop(heap)[1]
            elif b == str(-1):
                if len(heap) > 0:`
                    heappop(heap)[len(heap)-1]

        # print("heap = ", heap)

    if len(heap) == 0:
        print("EMPTY")
    else:
        print(heappop(heap)[1], heappop(heap)[len(heap)])
