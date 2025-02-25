import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(map(int, input().split()))

    for j in range(1, n+1):
        graph[i][j] = arr[j-1]

answer = copy.deepcopy(graph)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i>0:
            answer[i][j] += answer[i-1][j]
for i in range(1, n+1):
    for j in range(1, n+1):
        if j>0:
            answer[i][j] += answer[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = answer[x2][y2] - answer[x1-1][y2] - answer[x2][y1-1] + answer[x1-1][y1-1]
    print(result)