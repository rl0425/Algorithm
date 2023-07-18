import math

num = int(input())
max = int(math.sqrt(num))
count = 223
dp = [0 for _ in range(max+1)]

for cnt in range(1, max+1):
    dp[cnt] = cnt ** 2

temp = len(dp)

while temp != 0:
    temp2 = temp-1
    numTemp = num
    countTemp = 0

    while temp2 != 0:
        if dp[temp2] <= numTemp:
            numTemp -= dp[temp2]
            countTemp += 1
        else:
            temp2 -= 1

    if countTemp < count and countTemp != 0 and countTemp <= 4:
        count = countTemp

    temp -= 1

print(count)


