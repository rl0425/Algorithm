a = int(input())

d = [0] * a

if a == 1:
    print(1)

else:
    d[0] = 1
    d[1] = 2

    for x in range(2, a):
        d[x] = d[x-1] + d[x-2]

    print(d[a-1] % 10007)

# 20분