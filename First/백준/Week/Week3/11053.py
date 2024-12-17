a = int(input())
b = list(map(int, input().split()))

d = [0] * 1001

for x in range(len(b)):
    d[b[x]] = 1
    for y in range(x-1, -1, -1):
        if b[y] < b[x] and d[b[y]] >= d[b[x]]:
            d[b[x]] = d[b[y]] + 1

print(max(d))


