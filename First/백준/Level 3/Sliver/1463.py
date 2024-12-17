a = int(input())
d = [0 for _ in range(a+1)]

for x in range(2, a+1):
    d[x] = d[x-1] + 1

    if x % 3 == 0:
        d[x] = min(d[x], d[x//3] + 1)
    if x % 2 == 0:
        d[x] = min(d[x], d[x//2] + 1)

print(d[a])
