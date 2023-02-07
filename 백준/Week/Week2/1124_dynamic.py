import sys

a,b = map(int,sys.stdin.readline().split())
d = [False,False] + [True]*(999998)

for i in range(2,int(100000**0.5)+1):
  if d[i]:
    for j in range(2*i, b+1, i):
        d[j] = False

dArray = [0 for _ in range(b+1)]

for i in range(1, b+1):
    if d[i]:
        dArray[i] = 1

for i in range(2, b+1):
    for j in range(2, b+1):
        if i * j > b:
            break
        if d[j]:
            dArray[i*j] = dArray[i] + 1

answer_cnt = 0
for i in range(a,b+1):
    if d[dArray[i]]:
        answer_cnt += 1

print(answer_cnt)