a = int(input())
b = list(map(int,input().split()))

sorted = sorted(b)
num = 0
last = 0

for x in sorted:
    num = num + x
    last = last + num

print(last)

#  1분