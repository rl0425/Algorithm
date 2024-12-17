n, m = map(int, input().split())

graph = [i for i in range(m + 1)]

inputList = []

for x in range(n):
    inputList.append(list(map(int, input().split())))

for i in range(m + 1):
    if graph[i] > graph[i-1] + 1:
        graph[i] = graph[i-1] + 1

    for f, s, length in inputList:
        if i == f and s <= m:
            if graph[s] > graph[i] + length:
                graph[s] = graph[i] + length

print(graph[m])
