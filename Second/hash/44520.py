n = int(input())
has_card = list(map(int, input().split()))
m = int(input())
crt_card = list(map(int, input().split()))

arr = [0] * 20000001

for e in has_card:
    arr[e] = 1

for e in crt_card:
    if arr[e] == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')