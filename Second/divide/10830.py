
n, b = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        graph[i][j] = row[j]

def multiply(a, b):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += (a[i][k] * b[k][j]) % 1000
    return temp

def power(b):
    if b == 1:
        return graph
    temp = power(b//2)
    if b % 2 == 0:
        return multiply(temp, temp)
    else:
        return multiply(multiply(temp, temp), graph)

ans = power(b)
for i in range(n):
    print(*(x % 1000 for x in ans[i]))