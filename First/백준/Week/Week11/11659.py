import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = list(map(int, input().rstrip().split()))

array = [0 for x in range(a+1)]

for x in range(a):
    array[x+1] = array[x] + c[x]

for x in range(b):
    i, j = map(int, input().rstrip().split())

    print(array[j] - array[i-1])


