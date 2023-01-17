import sys
input = sys.stdin.readline

a, b = map(int, input().split())

nSet = set()
mSet = set()

for x in range(a):
    nSet.add(input())

for x in range(b):
    mSet.add(input())

aList = (list(map(lambda s : ''.join(s.split()), (nSet & mSet))))
aList = sorted(aList)

print(len(aList))
print(*aList)