import sys
input = sys.stdin.readline

answer = []

while True:
    inputData = []
    ans = True
    last = ""

    an = input()
    if an == ".\n":
        break

    for x in an:
        if x == "(" or x == "[":
            inputData.append(x)
            last = x
        elif x == ")" or x == "]":
            if last == "(" and x == ")":
                if len(inputData) > 0:
                    inputData.pop()

            elif last == "[" and x == "]":
                if len(inputData) > 0:
                    inputData.pop()

            else:
                inputData = []
                ans = False
                break

            if len(inputData) > 0:
                last = inputData[len(inputData)-1]
            elif len(inputData) == 0:
                last = ""

    if len(inputData) > 0 or ans == False:
        answer.append("no")
    else:
        answer.append("yes")

print(*answer)