import sys

input = sys.stdin.readline

a = int(input())
answerList = []


def bfs(data, value, correct):
    nowData = []

    flag = [-1] * 10000
    left = (data % 1000) * 10 + data // 1000
    right = (data % 10) * 1000 + data // 10
    dCount = (data * 2) % 10000
    sCount = (data - 1) % 10000

    nowData.append([dCount, value + "D"])
    nowData.append([sCount, value + "S"])
    nowData.append([right, value + "L"])
    nowData.append([left, value + "R"])

    flag[dCount] = 0
    flag[sCount] = 0
    flag[right] = 0
    flag[left] = 0

    while len(nowData) != 0:

        data = nowData.pop(0)
        # print(data)

        data[0] = int(data[0])

        # print("data = ", data)

        if correct == data[0]:return data[1]

        else:
            left = (data[0] % 1000) * 10 + data[0] // 1000
            right = (data[0] % 10) * 1000 + data[0] // 10
            dCount = (data[0] * 2) % 10000
            sCount = (data[0] - 1) % 10000

            if correct == dCount:return data[1] + "D"
            if correct == sCount:return data[1] + "S"
            if correct == right:return data[1] + "L"
            if correct == left:return data[1] + "R"

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
    x, y = map(int, input().split())
    value = ""

    answer = bfs(x, value, y)
    answerList.append(answer)

print(*answerList)