import re

a = int(input())

for x in range(a):
    b = input()
    c = int(input())
    d = re.findall(r'\d+', input())

    numList = []
    for x in d:
        numList.append(int(x))

    reverse = False
    error = False

    for y in range(len(b)):
        if b[y] == "R":
            reverse = not reverse
        else:
            if len(numList) != 0:
                if reverse:
                    i1 = numList.pop()
                else:
                    i2 = numList.pop(0)
            else:
                error = True

    if error:
        print("error")
    elif len(numList) == 0:
        print([])
    else:
        if reverse:
            numList = list(reversed(numList))

        print("[", end="")
        for x in range(len(numList)):
            if x == len(numList)-1:
                print(numList[x], end="")
            else:
                print(numList[x], end="")
                print(",", end="")
        print("]")



