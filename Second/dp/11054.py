n = int(input())
s = [[0] * 2 for _ in range(n)]
lst = list(map(int, input().split()))

for i in range(len(lst)):
    maxNum = 1
    for j in range(i, -1, -1):
        if lst[i] > lst[j]:
            maxNum = max(maxNum, s[j][0] + 1)
    s[i][0] = maxNum

for i in range(len(lst)-1, -1, -1):
    maxNum = 0
    for j in range(i, len(lst)):
        if lst[i] > lst[j]:
            maxNum = max(maxNum, s[j][1] + 1)
    s[i][1] = maxNum

max_num = max([x[0] + x[1] for x in s])
print(max_num)
