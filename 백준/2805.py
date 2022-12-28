a, b = map(int, input().split())

inputData=list(map(int,input().split()))

left = 0
right = max(inputData)

valueSum = 0

while True:
    valueSum = 0

    middle = (left + right) // 2

    for x in inputData:
        sum = x - middle
        if sum > 0:
            valueSum += sum

    if b <= valueSum:
        left = middle + 1
    elif b > valueSum:
        right = middle - 1

    if left > right:
        print(right)
        break


