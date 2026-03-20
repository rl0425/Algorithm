import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
current_sum = 0
end = 0

for start in range(n):
    while current_sum < m and end < n:
        current_sum += arr[end]
        end += 1

    if current_sum == m:
        ans += 1

    current_sum -= arr[start]

print(ans)