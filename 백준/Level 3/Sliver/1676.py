a = int(input())

if a == 0 or a == 1:
    print(0)

else:
    answer = 0
    num = 1
    value = 0

    for x in range(2, a+1, 1):
        num = num * x

        if int(str(num)[len(str(num))-1]) == 0:
            while True:
                num = int(num/10)

                answer += 1

                if int(str(num)[len(str(num))-1]) != 0:
                    num = int(str(num)[len(str(num))-1])
                    break
    print(answer)


# 30분