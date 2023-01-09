a,b,c = map(int,input().split())

total = (2**a) * (2**a)
quarter = total/4
half = (2**a)/2

sabun = 0

if b < half and c < half:
    sabun = 1

elif b < half and c >= half:
    sabun = 2

elif b >= half and c < half:
    sabun = 3

elif b >= half and c >= half:
    sabun = 4

boxX = b
boxY = c

if b >= half:
    boxX = int(b - half)
if c >= half:
    boxY = int(c - half)

quarterN = quarter // (half//2)

print("total = " , total)
print("quarter = ",quarter)
print("half = ", half)
print("boxX = ", boxX)
print("boxY = ", boxY)

print("(quarter * (sabun-1)) = ", (quarter * (sabun-1)))
print("(boxX // 2 * quarter) / 2 = ", (boxX // 2 * quarterN))
print("(boxY // 2 * 4) = ", (boxY // 2 * 4))
print("((boxX % 2) * 2) = ", ((boxX % 2) * 2))
print("(boxY % 2) = ", (boxY % 2))

print("(quarter * (sabun-1)) = ", (quarter * (sabun-1)))
a1 = (boxX // 4)
b1 = (boxY // 4)

if boxX % 4 == 1:
    a2 = 2
elif boxX % 4 == 2:
    a2 = 8
elif boxX % 4 == 3:
    a2 = 10

if boxY % 4 == 1:
    b2 = 1
elif boxY % 4 == 2:
    b2 = 4
elif boxY % 4 == 3:
    b2 = 5

print("a1 = ", a1)
print("a2 = ", a2)
print("b1 = ", b1)
print("b2 = ", b2)

print("hap = ", a1+a2+b1+b2+(quarter * (sabun-1)))


if a == 1:
    print(0)

else:
    quarterN = quarter // (half//2)

    sum = int((quarter * (sabun-1)) + (boxX // 2 * quarterN) + (boxY // 2 * 4) + ((boxX % 2) * 2) + (boxY % 2))

    print(sum)



#  다시