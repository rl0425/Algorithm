a = int(input())

inputData = [[] for _ in range(a)]
answer = []

def fun(arr):
    num = arr[0][0]
    correct = True

    global answer

    if len(arr) != 1:
        for x in range(len(arr[0])):
            if correct == False:
                break
            for y in range(len(arr[0])):
                if arr[x][y] != num:
                    answer.append("(")
                    twice = int(len(arr)/2)

                    one = [row[:twice] for row in arr[:twice]]
                    two = [row[:twice] for row in arr[twice:len(arr)]]

                    three = [row[twice:len(arr)] for row in arr[:twice]]
                    four = [row[twice:len(arr)] for row in arr[twice:len(arr)]]

                    fun(one)
                    fun(three)
                    fun(two)
                    fun(four)

                    answer.append(")")

                    correct = False
                    break

    if correct:
        answer.append(num)

for x in range(a):
    line = input()
    binary_list = [int(digit) for digit in str(line)]
    inputData[x] = binary_list

fun(inputData)

for x in range(len(answer)):
    print(answer[x], end='')
# print(*answer)
