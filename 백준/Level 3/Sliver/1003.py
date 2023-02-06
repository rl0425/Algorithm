a = int(input())

for x in range(a):
    num = int(input())
    d = [0] * (num+1)

    if num == 0:
        print(1, 0)
    elif num == 1:
        print(0, 1)
    else:
        d[0] = {"zero": 1, "first": 0}
        d[1] = {"zero": 0, "first": 1}
        d[2] = {"zero": 1, "first": 1}

        for y in range(3, num+1):
            d[y] = {"zero": d[y-1]["zero"] + d[y-2]["zero"],
                    "first": d[y-1]["first"] + d[y-2]["first"]}

        print(d[num]["zero"], d[num]["first"])
