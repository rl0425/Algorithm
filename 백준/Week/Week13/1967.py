import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())

tree = {}

def dfs(root, dist):
    for x in tree[root]:
        if distance[x[0]] == -1:
            distance[x[0]] = dist + x[1]
            dfs(x[0], dist + x[1])

for _ in range(n-1):
    # dict 생성
    s, e, d = map(int, input().split())

    if s not in tree:
        tree[s] = [(e,d)]
    else:
        tree[s].append((e,d))

    if e not in tree:
        tree[e] = [(s,d)]
    else:
        tree[e].append((s,d))

if n == 1:
    print(0)

else:
    # 첫번째 거리 구하기
    distance = [-1] * (n+1)
    distance[1] = 0
    dfs(1, 0)

    # 가장 긴 인덱스 설정
    maxIdx = distance.index(max(distance))

    # 두번째 거리 구하기
    distance = [-1] * (n+1)
    distance[maxIdx] = 0

    dfs(maxIdx, 0)

    print(max(distance))
