import sys
input = sys.stdin.readline
INF = float('inf')

def bellman_ford(n, edges):
    dist = [INF] * (n + 1)
    dist[1] = 0  # 시작 지점의 거리를 0으로 초기화

    # n-1번 반복
    for i in range(n - 1):
        for u, v, w in edges:
            print("u v w ", u,v,w)
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 확인
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return True  # 음수 사이클 존재

    print("dist= ", dist)

    return False  # 음수 사이클 없음

# 입력 처리
t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):  # 도로 입력
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))  # 양방향 도로

    for _ in range(w):  # 웜홀 입력
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))  # 웜홀은 음수 가중치

    # 결과 출력
    if bellman_ford(n, edges):
        print("YES")
    else:
        print("NO")
