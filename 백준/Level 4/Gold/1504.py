a = int(input())
b = int(input())

inputData = {}
visited = []

def dfs(graph, start):
    dfsArray = [start]

    while dfsArray:
        data = dfsArray.pop()
        if data not in visited:
            visited.append(data)
            if data in graph:
                temp = list(set(graph[data]) - set(visited))
                dfsArray += temp

for x in range(b):
    c, d = map(int,input().split())

    if c not in inputData:
        inputData[c] = [d]
    else:
        inputData[c].append(d)

    if d not in inputData:
        inputData[d] = [c]
    else:
        inputData[d].append(c)

dfs(inputData, 1)

print(len(visited)-1)


