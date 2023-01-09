a, b = map(int, input().split())

sum1 = 1
sum2 = 1

for x in range(b, a):
    sum1 = sum1 * (x+1)

for x in range(a-b):
    sum2 = sum2 * (x+1)

print(int(sum1/sum2))