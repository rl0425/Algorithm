a, b = map(int,input().split())

noSwitch = False
maxValue = 100 if a > 100 else a

answerArray = []

correct = False

if b > 101 or b < 2:
    print(-1)

else:
    for x in range(b, 101):
        sum = 0
        answerArray = []

        first = int((a/x) - x/2 + 1/2)

        if first < 0:
            answerArray.append(-1)
            break

        if isinstance(first, int):
            for y in range(0, x):
                sum += y+first
                answerArray.append(y+first)

        if sum == a:
            correct = True
            break

    if correct:
        print(*answerArray)
    else:
        print(-1)

# 조건 잘못봐서 2시간 걸림