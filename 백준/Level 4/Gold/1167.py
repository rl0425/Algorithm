import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

v = int(input())

# 배열 저장 트리
tree = [[] for _ in range(v+1)]

def dfs(start, depth):
    for n, d in tree[start]:
        # 아직 방문하지 않은 정점
        if distance[n] == -1:
            distance[n] = d + depth
            dfs(n, distance[n])

for _ in range(v):
    arr = list(map(int, input().split()))

    for x in range(len(arr)-1):
        # 특정 조건으로 정점 및 간선 구별
        if x % 2 == 1:
            tree[arr[0]].append((arr[x], arr[x+1]))

# 루트에서 가장 먼 정점 구하기
distance = [-1 for _ in range(v+1)]
distance[1] = 0
dfs(1, 0)

# 가장 먼 정점 인덱스 가져오기
maxIndex = distance.index(max(distance))

# 가장 먼 정점에서 가장 먼 정점 구하기
distance = [-1 for _ in range(v+1)]
distance[maxIndex] = 0
dfs(maxIndex, 0)

print(max(distance))
