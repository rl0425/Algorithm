n, k = map(int, input().split())

nList = list(map(int, input().split()))

nList.sort()

print(nList[k-1])