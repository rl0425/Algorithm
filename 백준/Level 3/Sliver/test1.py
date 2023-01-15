def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            print("n = ", n)
            print("graph[n] = ", graph[n])
            print("set(visited) = ", set(visited))
            print("graph[n] - set(visited) = ", graph[n] - set(visited))
            stack += graph[n] - set(visited)
            print("stack = ", stack)
    return visited

graph_list = {1: set([2,3,4]),
              2: set([4]),
              3: set([4]),
              # 4: set([1]),
              # 5: set([2, 6]),
              # 6: set([3, 5])}
              }
root_node = 1

print(DFS_with_adj_list(graph_list, root_node))