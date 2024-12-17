a = int(input())
inputData = []

maxFloor = 0
maxHo = 0
for x in range(a):
    a = int(input())
    b = int(input())

    if maxFloor < a:
        maxFloor = a
    if maxHo < b:
        maxHo = b

    inputData.append([a,b])

calc = []
num = []

for x in range(maxHo):
    num.append(x+1)

calc.append(num)

imsiCalc = []

for x in range(1, maxFloor+1):
    for y in range(maxHo):
        if y == 0:
            imsiCalc.append(1)
        else:
            imsiCalc.append(imsiCalc[y-1] + calc[x-1][y])

    calc.append(imsiCalc)

    imsiCalc = []

# print(calc)

for x in inputData:
    print(calc[x[0]][x[1]-1])
