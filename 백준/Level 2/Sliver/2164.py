from collections import deque

a = int(input())
num = 1

inputData = deque()

for x in range(a):
    inputData.append(x+1)



while True:
    if len(inputData) == 1:
        break

    inputData.popleft()
    inputData.append(inputData.popleft())

print(*inputData)