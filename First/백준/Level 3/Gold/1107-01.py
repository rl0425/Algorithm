# N = int(input())
# M = int(input())
# if M != 0:
#     broken = list(map(int, input().split()))
# else:
#     broken = []
# possible = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(broken)
#
# nowNum = 100
# result = 0
# btnResult = 0
#
# for x in str(N):
#     btnResult *= 10
#     flag = 10
#     target = -1
#     Nnum = int(x)
#     for y in possible:
#         tmp = abs(y - Nnum)
#         if flag > tmp:
#             target = y
#             flag = tmp
#     btnResult += target
#     result += 1
#
# print(min(result + abs(btnResult - N), abs(nowNum - N)))
#
#
#



N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = []
possible = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(broken)


topResult = 0
move = 0
for x in range(N, N + abs(N - 100), 1):
    if move > abs(N - 100):
        topResult = 500001
        break
    flag = True

    for y in set(str(x)):
        if int(y) not in possible:flag = False

    if flag:
        topResult = len(str(x)) + move
        break
    move += 1
if topResult == 0:topResult = 500001

downResult = 0
move = 0
for x in range(N, -1, -1):
    if move > topResult or move > abs(N - 100):break
    flag = True

    for y in set(str(x)):
        if int(y) not in possible: flag = False

    if flag:
        downResult = len(str(x)) + move
        break
    move += 1
if downResult == 0:downResult = 500001

print(min(downResult, topResult, abs(N - 100)))