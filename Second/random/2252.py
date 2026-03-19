import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
arr = {}

ans = []

def DFS(arr, start):
    list = [start]

    while list:
        d1 = list.pop()
        if len(arr[d1]) == 0:
            if not visited[d1]:
                ans.append(d1)
            visited[d1] = True
        else:
            list.extend([d1, *arr[d1]])
            arr[d1] = []

for i in range(1, n+1):
    arr[i] = []

for _ in range(m):
    v, k = map(int, input().split())

    if v not in arr[k]:
        arr[k].append(v)

for i in range(1, n+1):
    DFS(arr, i)

print(*ans)
