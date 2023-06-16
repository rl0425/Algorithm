a = int(input())

if a == 0:
    print(0)

elif a == 1:
    print(1)

else:
    d = [0 for _ in range(a)]
    d[0] = 1
    d[1] = 3
    for x in range(2, a):
        d[x] = d[x-1] + d[x-2] * 2

    print((d[-1]) % 10007)