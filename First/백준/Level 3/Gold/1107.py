a = int(input())
b = int(input())

if b != 0:
    c = input().split()

minAppend = []

if a == 100:
    minAppend.append(0)

elif b == 0:
    minusValue = 0

    if a > 100:
        minusValue = a - 100
    else:
        minusValue = 100 - a

    if minusValue > len(str(a)):
        minAppend.append(len(str(a)))
    else:
        minAppend.append(minusValue)

else:
    for x in range(a, -1, -1):
        success = True
        for y in range(len(str(x))):
            if str(x)[y] in c:
                success = False
                break

        if success:
            minAppend.append(int(len(str(x)) + a-x))
            break

    for x in range(a, 1000001):
        success = True
        for y in range(len(str(x))):
            if str(x)[y] in c:
                success = False
                break

        if success:
            minAppend.append(int(len(str(x)) + x-a))
            break

# if len(minAppend) == 0:
if a > 100:
    minAppend.append(a-100)
else:
    minAppend.append(100-a)

print(min(minAppend))