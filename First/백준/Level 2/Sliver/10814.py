import sys
input = sys.stdin.readline

a = int(input())
inputData = []

for x in range(a):
    inputData.append(list(input().split()))

for x in range(len(inputData)):
    inputData[x].append(x)


answer = sorted(inputData, key = lambda x : (int(x[0]), x[2]))

for x in range(len(answer)):
    print(answer[x][0], answer[x][1])