a, b = map(int, input().split())

inputData = [i+1 for i in range(a)]
answer = ""

while len(inputData) != 0:
    for x in range(1,b):
        inputData.append(inputData.pop(0))

    if answer == "":
        strData = str(inputData.pop(0))

        if len(inputData) == 0:
            answer = strData
        else:
            answer = strData + ", "

    else:
        strData = str(inputData.pop(0))

        if len(inputData) == 0:
            answer = answer + strData
        else:
            answer = answer + strData + ", "

print("<",end="")
print(answer,end="")
print(">",end="")




