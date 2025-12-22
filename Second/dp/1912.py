# 25/12/22

n = int(input())
lst = list(map(int, input().split()))
s = [0 for _ in range(n)]
ans = lst[0]

for i in range(len(lst)):
    s[i] = lst[i]
    if s[i-1] > 0:
        s[i] += s[i-1]
    if ans < s[i]:
        ans = s[i]
print(ans)