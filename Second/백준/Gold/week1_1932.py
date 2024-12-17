num_lines = int(input())
inputList = []
for _ in range(num_lines):
    line = list(map(int, input().split()))
    inputList.append(line)
for i in range(len(inputList)):
    for j in range(len(inputList[i])):
        if j == 0:
            if i != 0:
                inputList[i][j] += inputList[i-1][j]
        else:
            if i == 1:
                inputList[i][j] += inputList[i-1][j-1]
            elif j == len(inputList[i]) - 1:
                inputList[i][j] += inputList[i - 1][j - 1]
            else:
                inputList[i][j] += max(inputList[i-1][j-1], inputList[i-1][j])

maxNum = max(inputList[-1])
print(maxNum)

# 20min