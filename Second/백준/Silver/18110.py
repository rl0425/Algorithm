import sys

n = int(input())
def new_round(num):
    return int(num + 0.5)
answerList = []
for _ in range(n):
    answerList.append(int(sys.stdin.readline()))
exception = int(new_round(n * 0.15))
answerList = sorted(answerList)
level = answerList
if exception > 0:
    level = answerList[exception:-exception]
if n == 0:
    print(0)
else:
    print(new_round(sum(level)/len(level)))