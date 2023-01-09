import sys
input = sys.stdin.readline

a = int(input())
inputData = []

for x in range(a):
    inputData.append(int(input()))

inputData.sort()

print(*inputData)