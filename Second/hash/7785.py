n = int(input())
dic = {}

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        dic[name] = 1
    if state == 'leave':
        dic[name] = 0
dic = dict(sorted(dic.items(), reverse=True))

for key, value in dic.items():
    if value == 1:
        print(key)