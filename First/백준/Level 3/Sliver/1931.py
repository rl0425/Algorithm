import sys, heapq
input = sys.stdin.readline

a = int(input())
inputData = []

for x in range(a):
    b,c = map(int, input().split())
    inputData.append([b, c])

inputData = sorted(inputData, key = lambda x : (x[1], x[0]))

start = inputData[0]
count = 1

for x in range(1,len(inputData)):
    if inputData[x][0] >= start[1]:
        start = inputData[x]
        count += 1

print(count)