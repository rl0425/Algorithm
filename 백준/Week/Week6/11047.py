a,b = map(int, input().split())
inputData = []

sum = 0

now = int(b)
num = 0

for x in range(a):
    inputData.append(int(input()))

for x in range(a-1,-1,-1):

    if now // inputData[x] > 0:
        mok = now // inputData[x]
        now = now - (mok*inputData[x])
        num += mok

    if now == 0:
        break;

print(num)


# 10분