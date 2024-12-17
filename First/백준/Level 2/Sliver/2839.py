a = int(input())

max = a // 5

five = 0
three = 0

while True:
    if max == 0:
        if (a - (max * 5)) % 3 == 0:
            five = 0
            three = a // 3
            break
        else:
            five = 0
            three = 0
            break

    namuge = a - (max * 5)

    if namuge % 3 == 0:
        five = max
        three = namuge // 3
        break

    else:
        max -= 1

answer = five + three
if answer == 0:
    print(-1)
else:
    print(answer)
