a = int(input())

if a == 1:
    print(1)

else:
    num = 1
    count = 1
    while True:
        num += count*6

        if a <= num:
            print(count+1)
            break
        else:
            count += 1