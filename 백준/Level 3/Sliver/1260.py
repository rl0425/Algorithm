from collections import deque

a,b,c = map(int, input().split())
def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        value = stack.pop()
        if value not in visited:
            visited.append(value)
            if value in graph:
                temp = list(set(graph[value]) - set(visited))
                temp = sorted(temp, reverse=True)
                stack += temp

    return visited

def bfs(graph, v):
    visited = []
    queue = deque([v])

    while queue:
        value = queue.popleft()

        if value not in visited:
            visited.append(value)
            if value in graph:
                temp = list(set(graph[value]) - set(visited))
                temp = sorted(temp, reverse=False)
                queue += temp

    return visited

graph = {}

for x in range(b):
    d, e = map(int,input().split())

    if d not in graph:
        graph[d] = [e]
    elif e not in graph[d]:
        graph[d].append(e)

    if e not in graph:
        graph[e] = [d]
    elif d not in graph[e]:
        graph[e].append(d)

print(*dfs(graph,c))
print(*bfs(graph,c))