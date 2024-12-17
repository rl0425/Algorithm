a = int(input())
b = list(map(int,input().split()))

answerList = []
count = 0

inputList = []

for x in range(len(b)):
    inputList.append([b[x], x])

while len(inputList) != 0:
    first = inputList.pop(0)
    count += 1

    answerList.append(first[1]+1)

    if len(inputList) == 0:
        break

    if first[0] > 0:
        for x in range(first[0]-1):
            num = inputList.pop(0)
            inputList.append(num)

    elif first[0] < 0:
        for x in range(abs(first[0])):
            inputList.insert(0, inputList.pop())

print(*answerList)