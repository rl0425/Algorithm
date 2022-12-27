c, d = map(int, input().split())

inputData = []

answer = []

for x in range(c):
    inputData.append(input())

inputDataCopy = []
inputDataCopy.extend(inputData)

def func(y, x, type):
    count = 0

    if type == "B":
        if inputData[y][x] == "W":
            count += 1
            my_list = list(inputData[y])
            my_list[x] = 'B'
            inputData[y] = ''.join(my_list)


    elif type == "W":
        if inputData[y][x] == "B":
            count += 1
            my_list = list(inputData[y])
            my_list[x] = 'W'
            inputData[y] = ''.join(my_list)

    for a in range(8):
        for b in range(8):
            if a > 0 and b == 0:
                if inputData[a - 1 + y][b + x] == inputData[a + y][b + x]:
                    count += 1
                    if inputData[a + y][b + x] == "B":
                        my_list = list(inputData[a + y])
                        my_list[b + x] = 'W'
                        inputData[a + y] = ''.join(my_list)

                    elif inputData[a + y][b + x] == "W":
                        my_list = list(inputData[a + y])
                        my_list[b + x] = 'B'
                        inputData[a + y] = ''.join(my_list)

            if b > 0:
                if inputData[a + y][b - 1 + x] == inputData[a + y][b + x]:
                    count += 1

                    if inputData[a + y][b + x] == "B":
                        my_list = list(inputData[a + y])
                        my_list[b + x] = 'W'
                        inputData[a + y] = ''.join(my_list)

                    elif inputData[a + y][b + x] == "W":
                        my_list = list(inputData[a + y])
                        my_list[b + x] = 'B'
                        inputData[a + y] = ''.join(my_list)


    answer.append(count)



for x in range(d-7):
    for y in range(c-7):
        func(y, x, "B")
        inputData = []
        inputData.extend(inputDataCopy)

        func(y, x, "W")
        inputData = []
        inputData.extend(inputDataCopy)


print(min(answer))

