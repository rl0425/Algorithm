for x in range(int(input())):
    hash = {}
    num = 1

    for y in range(int(input())):
        c, d = input().split()

        if d not in hash:
            hash[d] = 2
        else:
            hash[d] += 1

    result = list(hash.values())

    for y in result:
        num *= y

    print(num - 1)
