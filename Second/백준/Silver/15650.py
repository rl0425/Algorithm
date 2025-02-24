from itertools import combinations
n, m = map(int, input().split())
comb = list(combinations([i for i in range(1, n+1)], m))

for c in comb:
    print(*c)
