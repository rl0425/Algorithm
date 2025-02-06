from collections import deque

def bfs(graph):
    queue = deque()
    queue.append(1)
    parent_arr = [0] * (n+1)

    while queue:
        parent = queue.popleft()
        for child in graph[parent]:
            if child != 1 and parent_arr[child] == 0:
                parent_arr[child] = parent
                queue.append(child)

    return parent_arr

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = bfs(graph)
for i in range(len(parent)):
    if i > 1:
        print(parent[i])
