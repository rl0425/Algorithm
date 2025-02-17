n = int(input())
INF = 1e8

for _ in range(n):
    n,m,w = map(int, input().split())
    arr = [[float('inf')] * (n+1) for _ in range(n+1)]
    answer = "NO"
    distance = [INF] * (n+1)

    for _ in range(m):
        a,b,c = map(int, input().split())
        if arr[a][b] > c:
            arr[a][b] = c
        if arr[b][a] > c:
            arr[b][a] = c

    for _ in range(w):
        a,b,c = map(int, input().split())
        arr[a][b] = -c
    print("arr =", arr)

    # for i in range(n):
    #     for j in range(m+w):
    #


    # for _ in range(w):
    #     a, b, c = map(int, input().split())
    #     if arr[b][a] < c:
    #         answer = "YES"
    print(answer)