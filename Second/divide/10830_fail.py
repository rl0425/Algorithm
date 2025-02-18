import copy

n, b = map(int, input().split())

graph = [[0] * n for _ in range(n)]

def procession(i, j):
    sum = 0
    for cnt in range(n):
        sum += (cal_graph[i][cnt] * graph[cnt][j]) % 1000
    return sum

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        graph[i][j] = row[j]
cal_graph = copy.deepcopy(graph)

for _ in range(b-1):
    temp_graph = copy.deepcopy(cal_graph)
    for i in range(n):
        for j in range(n):
            temp_graph[i][j] = procession(i, j)
    cal_graph = temp_graph

for i in range(n):
    print(*(x % 1000 for x in cal_graph[i]))

