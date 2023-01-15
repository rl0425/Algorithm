a,b = map(int,input().split())

noSwitch = False

answer = [-1]

for x in range(a, 0, -1):
    num = a
    nList = []
    for y in range(x, 0, -1):
        if num - y < 0:
            nList = []
            break
        else:
            num -= y
            nList.append(y)

            if num == 0:
                break

    if noSwitch:
        answer.append(-1)
        break

    if len(nList) >= b:
        max = 0
        for x in nList:
            max += x

        if max == a:
            answer = nList
        break


answer = sorted(answer, reverse=False)

print(answer)