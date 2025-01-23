import sys

n = int(input())
data = {i:0 for i in range(1, 10001)}
for i in range(n):
    trash = int(sys.stdin.readline())
    data[trash] += 1

for key, value in data.items(): #최대 10,000
    if value > 0:
        for v in range(value): #최대 10,000,000
            sys.stdout.write(str(key) + "\n")  # 개행 추가