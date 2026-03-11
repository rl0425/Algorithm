n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
sum = 0

min = price[0]

for i in range(0, len(price)-1):
    if price[i] < min:
        min = price[i]
    sum += min * road[i]

print(sum)