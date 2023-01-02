a = input()

num = '666'
count = 0

while True:
    sixCount = 0
    for x in range(len(num)):
        if int(num[x]) == 6:
            sixCount += 1

        else:
            sixCount = 0

        if sixCount == 3:
            count += 1
            break

    if int(count) == int(a):
        print(num)
        break

    else:
        num = str(int(num) + 1)
