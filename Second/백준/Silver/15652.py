import itertools
n, m = map(int, input().split())
arr = itertools.combinations_with_replacement([i for i in range(1, n+1)], m)

for e in list(arr):
    print(*e)
