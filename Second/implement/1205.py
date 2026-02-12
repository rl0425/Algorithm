import sys

# 입력 받기
input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
new_score = int(input_data[1])
p = int(input_data[2])

if n == 0:
    print(1)
    exit()

scores = list(map(int, input_data[3:]))

if n == p and new_score <= scores[-1]:
    print(-1)
else:
    rank = 1
    for s in scores:
        if s > new_score:
            rank += 1
        else:
            break
    print(rank)