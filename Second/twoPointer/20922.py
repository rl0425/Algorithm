n, k = map(int, input().split())
s = list(map(int, input().split()))

has_arr = [0] * 1000001
dist = 0
left = 0
answer = 0
max_num = 0

for right in range(n):
    if has_arr[s[right]] == 0:
        dist += 1
    has_arr[s[right]] += 1
    if has_arr[s[right]] > k:
        while has_arr[s[right]] > k:
            has_arr[s[left]] -= 1
            if has_arr[s[left]] == 0:
                dist -= 1
            left += 1
    max_num = max(max_num, right - left + 1)

print(max_num)