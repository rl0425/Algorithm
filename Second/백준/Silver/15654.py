import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp_arr = list(set(itertools.combinations_with_replacement(arr, m)))
arr = set([])
for ans in temp_arr:
    ans = list(ans)
    ans.sort()
    arr.add(tuple(ans))
arr = list(arr)
arr.sort()
for ans in arr:
    print(*ans)