a = int(input())

alist = []

for x in range(a):
    b = input()
    alist.append(b)

alist = set(alist)
lists = sorted(alist, key = lambda x : (len(x), x) )

for i in lists:
    print(i)
