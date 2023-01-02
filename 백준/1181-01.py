a = int(input())

# 코드를 줄이긴 하되 원본과의 효율성 차이는 미미함
alist = set()
for x in range(int(input())):alist.add(input())
print(*sorted(alist, key = lambda x : (len(x), x) ))
