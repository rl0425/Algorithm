import sys
input = sys.stdin.readline
inf = sys.maxsize

V, E = map(int, input().split())
graph = [[inf] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(V):
    answer = min(answer, graph[i][i])
print(-1 if answer == inf else answer)


import sys
input = sys.stdin.readline
inf = sys.maxsize


def get_min_cost_cycle(graph: list[list[int]], vertex_count: int) -> int:
    min_cost_cyle = sys.maxsize
    for middle in range(vertex_count):
        for start in range(vertex_count):
            for end in range(vertex_count):
                if graph[start][end] > graph[start][middle] + graph[middle][end]:
                    graph[start][end] = graph[start][middle] + graph[middle][end]
    for i in range(vertex_count):
        min_cost_cyle = min(min_cost_cyle, graph[i][i])
    return min_cost_cyle if min_cost_cyle != inf else -1

def main():
    vertex_count, edge_count = map(int, input().split())
    graph = [[inf] * vertex_count for _ in range(vertex_count)]
    for _ in range(edge_count):
        start, end, cost = map(int, input().split())
        graph[start - 1][end - 1] = cost
    print(get_min_cost_cycle(graph, vertex_count))

if __name__ == "__main__":
    main()