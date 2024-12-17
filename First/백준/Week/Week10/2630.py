a = int(input())

inputData = [[] for _ in range(a)]
oneAnswer = 0
zeroAnswer = 0

def fun(arr):
    num = arr[0][0]
    correct = True

    global oneAnswer, zeroAnswer

    if len(arr) != 1:
        for x in range(len(arr[0])):
            if correct == False:
                break
            for y in range(len(arr[0])):
                if arr[x][y] != num:
                    twice = int(len(arr)/2)

                    one = [row[:twice] for row in arr[:twice]]
                    two = [row[:twice] for row in arr[twice:len(arr)]]

                    three = [row[twice:len(arr)] for row in arr[:twice]]
                    four = [row[twice:len(arr)] for row in arr[twice:len(arr)]]

                    fun(one)
                    fun(three)
                    fun(two)
                    fun(four)

                    correct = False
                    break

    if correct:
        if num == "0":
            zeroAnswer += 1
        elif num == "1":
            oneAnswer += 1

for x in range(a):
    line = input().split()

    # binary_list = [int(digit) for digit in str(line)]
    inputData[x] = line

fun(inputData)

print(zeroAnswer)
print(oneAnswer)
