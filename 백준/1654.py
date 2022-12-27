a, b = map(int, input().split())

inputData = []

for x in range(a):
    c = input()
    inputData.append(int(c))

left = 1
right = max(inputData)
valueSum = 0

while True:
    valueSum = 0

    middle = (left + right) // 2

    for x in inputData:
        valueSum += x // middle

    if b <= valueSum:
        left = middle + 1
    elif b > valueSum:
        right = middle - 1

    if left > right:
        print(right)
        break


