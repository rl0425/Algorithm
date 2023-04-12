a, b = map(int, input().split())
inputData = []


def calculator(array):
    num = 0
    if a == 0 and b == 0:
        return -1

    if a < 3 or b < 3:
        for y in range(b):
            for x in range(a):
                if array[x][y] != array[x + a][y]:
                    return -1
        return 0

    elif a == 3 and b == 3:
        Reverse = False
        for y in range(b):
            for x in range(a):
                if array[x][y] != array[x + a][y]:
                    Reverse = True

        if Reverse:
            array = reverse(0, 0, array)
            num += 1

    else:
        for y in range(b - 1):
            for x in range(a - 1):
                if array[x][y] != array[x + a][y]:
                    if x + 2 >= a or y + 2 >= b:
                        return -1
                    else:
                        array = reverse(x, y, array)
                        num += 1

    for y in range(b):
        for x in range(a):
            if array[x][y] != array[x + a][y]:
                return -1

    return num

def reverse(xIndex, yIndex, array):
    fx = xIndex
    fy = yIndex
    for xIndex in range(fx, fx + 3):
        for yIndex in range(fy, fy + 3):
            if xIndex < a and yIndex < b:
                if array[xIndex][yIndex] == 1:
                    array[xIndex][yIndex] = 0
                elif array[xIndex][yIndex] == 0:
                    array[xIndex][yIndex] = 1

    return array


for i in range(a * 2):
    input_line = input()
    row = [int(char) for char in input_line]
    inputData.append(row)

print(calculator(inputData))
