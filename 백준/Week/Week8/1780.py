a = int(input())

inputData = [[] for _ in range(a)]

minus = 0
zero = 0
plus = 0

def fun(arr):
    global minus, zero, plus
    num = arr[0][0]
    correct = True

    if len(arr) != 1:
        for x in range(len(arr[0])):
            if correct == False:
                break
            for y in range(len(arr[0])):
                if arr[x][y] != num:
                    triple = int(len(arr)/3)

                    one = [row[:triple] for row in arr[:triple]]
                    two = [row[:triple] for row in arr[triple:triple*2]]
                    three = [row[:triple] for row in arr[triple*2:len(arr)]]

                    four = [row[triple:triple*2] for row in arr[:triple]]
                    five = [row[triple:triple*2] for row in arr[triple:triple * 2]]
                    six = [row[triple:triple*2] for row in arr[triple * 2:len(arr)]]

                    sev = [row[triple * 2:len(arr)] for row in arr[:triple]]
                    eig = [row[triple * 2:len(arr)] for row in arr[triple:triple * 2]]
                    nine = [row[triple * 2:len(arr)] for row in arr[triple * 2:len(arr)]]

                    fun(one)
                    fun(two)
                    fun(three)

                    fun(four)
                    fun(five)
                    fun(six)

                    fun(sev)
                    fun(eig)
                    fun(nine)

                    correct = False
                    break

    if correct:
        if num == -1:
            minus += 1
        elif num == 0:
            zero += 1
        elif num == 1:
            plus += 1

for x in range(a):
    inputData[x] = list(map(int, input().split()))

fun(inputData)

print(minus)
print(zero)
print(plus)