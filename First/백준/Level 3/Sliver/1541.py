a = input()

value = ""
minusMode = False
sum = 0
tempSum = 0

for x in a:
    if x == "+":
        if minusMode:
            tempSum += int(value)
        else:
            sum += int(value)

        value = ""
    elif x == "-":
        if minusMode:
            tempSum += int(value)
            sum -= tempSum
            tempSum = 0
        else:
            sum += int(value)

        value = ""
        minusMode = True
    else:
        value += x

if minusMode:
    tempSum += int(value)
    sum -= tempSum
else:
    sum += int(value)

print(sum)