n, m = map(int, input().split())

graph = []
dist = [float('inf')] * (n+1)
dist[1] = 0
def bell():
    for i in range(n):
        for s, e, t in graph:
            if dist[s] != float('inf') and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n - 1:
                    print("-1")
                    return
    for i in range(2, n+1):
        if dist[i] == float('inf'):
            print("-1")
        else:
            print(dist[i])
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

bell()