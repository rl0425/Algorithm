import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
input_arr = []
arr = [0] * (d+1)

for _ in range(n):
    input_arr.append(int(input()))

input_arr.extend(input_arr[:k])

dist = 0

for x in range(k):
    arr[input_arr[x]] += 1
    if arr[input_arr[x]] == 1:
        dist += 1

# 첫 구간 확인
curr = dist
if arr[c] == 0:
    curr += 1
max_num = curr

for start in range(k, n+k):
    arr[input_arr[start-k]] -= 1
    if arr[input_arr[start-k]] == 0:
        dist -= 1
    if arr[input_arr[start]] == 0:
        dist += 1
    arr[input_arr[start]] += 1
    curr = dist
    if arr[c] == 0:
        curr += 1
    max_num = max(max_num, curr)

print(max_num)
