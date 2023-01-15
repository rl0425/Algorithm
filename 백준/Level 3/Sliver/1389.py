a,b = map(int, input().split())


def bfs(graph, v):
    visited = []
    queue = [v]

    depth = {v: 0}
    sum = 0
    while queue:
        value = queue.pop(0)
        count = depth[value]

        if value not in visited:
            visited.append(value)
            plusData = set(graph[value]) - set(visited)
            queue += plusData
            for data in plusData:
                if data not in depth:
                    depth[data] = count+1

                    sum += depth[data]

    return sum

graph = {}
for x in range(b):
    c,d = map(int, input().split())

    if c not in graph:
        graph[c] = [d]
    elif d not in graph[c]:
        graph[c].append(d)

    if d not in graph:
        graph[d] = [c]
    elif c not in graph[d]:
        graph[d].append(c)


minValue = 0
num = 0
for x in range(1,a+1):
    if minValue == 0:
        minValue = bfs(graph,x)
        num = x

    if bfs(graph,x) < minValue:
        minValue = bfs(graph,x)
        num = x

print(num)