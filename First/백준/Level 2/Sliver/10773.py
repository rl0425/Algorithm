a = int(input())
inputList = []

for x in range(a):
    data = int(input())
    if data == 0:
        inputList.pop()
    else:
        inputList.append(data)

answer = 0
for x in inputList:
    answer += x

print(answer)