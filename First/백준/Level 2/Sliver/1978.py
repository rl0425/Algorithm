a = int(input())
b = list(map(int, input().split()))

count = 0
for x in b:
    type = True

    if x < 2:
        type = False

    else:
        for y in range(2, int(x ** 0.5)+1):
            if x % y == 0:
                type = False
                break

    if type:
        count += 1

print(count)