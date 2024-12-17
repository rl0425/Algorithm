a = int(input())

first = []
second = []

answer = []

for x in range(a):
    num, order = map(int, input().split())
    orderList = list(map(int, input().split()))

    first.append({
        1: num,
        2: order
    })

    second.append(orderList)


for x in range(len(first)):
    value = first[x][2]
    count = 1
    y = 0

    while True:
        if second[x][y] != max(second[x]):
            second[x].append(second[x].pop(0))

            if value == y:
                value = len(second[x])-1
            elif value != y:
                value -= 1

        else:
            second[x].pop(0)

            if value == y:
                answer.append(count)
                break
            elif value != y:
                count += 1
                value -= 1

print(*answer)


