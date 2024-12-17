import sys
input = sys.stdin.readline

a = int(input())
answerList = []

def bfs(data, value, correct):
    nowData = []
    flag = [-1] * 10000

    left = list(str(data))

    if len(left) == 1:
        left.insert(0, "0")
        left.insert(0, "0")
        left.insert(0, "0")

    elif len(left) == 2:
        left.insert(0, "0")
        left.insert(0, "0")
    elif len(left) == 3:
        left.insert(0, "0")

    left.insert(0, left.pop())
    right = list(str(data))

    if len(right) == 1:
        right.insert(0, "0")
        right.insert(0, "0")
        right.insert(0, "0")

    elif len(right) == 2:
        right.insert(0, "0")
        right.insert(0, "0")
    elif len(right) == 3:
        right.insert(0, "0")

    right.append(right.pop(0))

    tmp = ""
    for x in left:
        tmp += x

    left = int(tmp)

    tmp = ""
    for x in right:
        tmp += x

    right = int(tmp)

    dCount = data * 2
    if dCount >= 10000:
        dCount = dCount % 10000

    sCount = data - 1
    if int(sCount) < 0:
        sCount = 9999

    nowData.append([dCount, value+"D"])
    nowData.append([sCount, value+"S"])
    nowData.append([right, value+"L"])
    nowData.append([left, value+"R"])

    flag[int(dCount)] = 0
    flag[int(sCount)] = 0
    flag[int(right)] = 0
    flag[int(left)] = 0

    while len(nowData) != 0:

        data = nowData.pop(0)
        data[0] = int(data[0])

        if correct == data[0]:
            return data[1]
            break

        else:
            left = list(str(data[0]))

            if len(left) == 1:
                left.insert(0, "0")
                left.insert(0, "0")
                left.insert(0, "0")
            elif len(left) == 2:
                left.insert(0, "0")
                left.insert(0, "0")
            elif len(left) == 3:
                left.insert(0, "0")

            left.insert(0,left.pop())

            right = list(str(data[0]))

            if len(right) == 1:
                right.insert(0, "0")
                right.insert(0, "0")
                right.insert(0, "0")
            elif len(right) == 2:
                right.insert(0, "0")
                right.insert(0, "0")
            elif len(right) == 3:
                right.insert(0, "0")

            right.append(right.pop(0))

            tmp = ""
            for x in left:
                tmp += x

            left = int(tmp)

            tmp = ""
            for x in right:
                tmp += x

            right = int(tmp)

            dCount = data[0] * 2
            if dCount >= 10000:
                dCount = dCount % 10000

            sCount = data[0] - 1
            if sCount < 0:
                sCount = 9999

            if correct == dCount:
                return data[1] + "D"
                break
            if correct == sCount:
                return data[1] + "S"
                break
            if correct == right:
                return data[1] + "L"
                break
            if correct == left:
                return data[1] + "R"
                break

            else:
                if flag[dCount] == -1:
                    nowData.append([dCount, data[1] + "D"])
                    flag[dCount] = 0
                if flag[sCount] == -1:
                    nowData.append([sCount, data[1] + "S"])
                    flag[sCount] = 0
                if flag[right] == -1:
                    nowData.append([right, data[1] + "L"])
                    flag[right] = 0
                if flag[left] == -1:
                    nowData.append([left, data[1] + "R"])
                    flag[left] = 0


for x in range(a):
    x,y = map(int, input().split())
    value = ""

    answer = bfs(x, value, y)
    answerList.append(answer)

print(*answerList)