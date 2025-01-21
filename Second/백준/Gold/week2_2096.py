import copy

def maxScore(list):
    list = copy.deepcopy(list)
    for i in range(1, len(list)):
        for j in range(3):
            if j == 0:
                list[i][j] += max(list[i-1][j], list[i-1][j+1])
            if j == 1:
                list[i][j] += max(list[i-1][j], list[i-1][j+1], list[i-1][j-1])
            if j == 2:
                list[i][j] += max(list[i-1][j], list[i-1][j-1])
    return max(list[len(list)-1])

def minScore(list):
    list = copy.deepcopy(list)
    for i in range(1, len(list)):
        for j in range(3):
            if j == 0:
                list[i][j] += min(list[i-1][j], list[i-1][j+1])
            if j == 1:
                list[i][j] += min(list[i-1][j], list[i-1][j+1], list[i-1][j-1])
            if j == 2:
                list[i][j] += min(list[i-1][j], list[i-1][j-1])

    return min(list[len(list)-1])

n = int(input())
inputList = []

for x in range(n):
    inputList.append(list(map(int, input().split())))

max = maxScore(inputList)
min = minScore(inputList)
print(max, min)

# 메모리 실패
# 메모리 계산법 유추해보기