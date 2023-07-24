import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

v = int(input())

tree = [[] for _ in range(v+1)]

def dfs(start, depth):

    for n, d in tree[start]:
        if distance[n] == -1:
            distance[n] = d + depth
            dfs(n, distance[n])

for _ in range(v):
    arr = list(map(int, input().split()))

    for x in range(len(arr)-1):
        if x % 2 == 1:
            tree[arr[0]].append((arr[x], arr[x+1]))

distance = [-1 for _ in range(v+1)]
distance[1] = 0
dfs(1, 0)

maxIndex = distance.index(max(distance))

distance = [-1 for _ in range(v+1)]
distance[maxIndex] = 0
dfs(maxIndex, 0)

print(max(distance))
