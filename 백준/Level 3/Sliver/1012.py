num = int(input())
inputData = set()


for x in range(num):
    count = 0
    a, b, c = map(int,input().split())

    for y in range(c):
        a, b = map(int, input().split())

        inputData.add((a,b))

    while len(inputData) != 0:
        data = inputData.pop()

        print("data = ", data)
        print("inputData = ", inputData)

        for up in range(data[0], 0, -1):
            print("up = ", up)
            print("z[1] = ", data[1])
            if (up, data[1]) in inputData:
                inputData.remove((up, data[1]))
            else:
                break

        count += 1


