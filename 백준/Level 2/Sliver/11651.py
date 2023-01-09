import sys
input = sys.stdin.readline

num = int(input())
inputData = []

for x in range(num):
    a,b = map(int, input().split())
    inputData.append([a,b])

answer = sorted(inputData, key = lambda x : (x[1], x[0]))

for x in answer:
    print(x[0], x[1])
