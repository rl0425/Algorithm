numInput = int(input())

inputList = dict()

maxNum = "A"
minNum = "B"

for number in range(numInput):
    num = int(input())
    for x in range(num):
        a, b = input().split()

        if a == "I":
            if len(inputList) == 0:
                inputList[maxNum] = b
            elif len(inputList) == 1:

                if inputList[maxNum] > b:
                    inputList[minNum] = b
                else:
                    firstMax = inputList[maxNum]
                    inputList[maxNum] = b
                    inputList[minNum] = firstMax
            else:
                if inputList[maxNum] < b:
                    beforeMax = inputList.pop(maxNum)
                    inputList[maxNum] = b
                    inputList[beforeMax] = beforeMax
                elif inputList[minNum] and inputList[minNum] > b:
                    beforeMin = inputList.pop(minNum)
                    inputList[minNum] = b
                    inputList[beforeMin] = beforeMin
                else:
                    inputList[b] = b
        elif a == "D":
            if len(inputList) > 0:
                if b == str(1):
                    if len(inputList) > 0:
                        inputList.pop(maxNum)

                    if len(inputList) >= 1:
                        inputList[maxNum] = max(inputList)

                elif b == str(-1):
                    if len(inputList) > 1:
                        inputList.pop(minNum)
                    elif len(inputList) == 1:
                        inputList.pop(maxNum)

                    if len(inputList) > 1:
                        inputList[minNum] = min(inputList)


        # print("inputList = ", inputList)
        # print("inputList = ", inputList[maxNum])
    if len(inputList) == 0:
        print("EMPTY")
    else:
        print("inputList = ", inputList)
        print(inputList[maxNum], inputList[minNum])