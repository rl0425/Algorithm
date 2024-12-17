a,b,c,d = map(int, input().split())

numList = [a,b]

if a-c < 0:
    numList.append(-(a-c))
else:
    numList.append(a - c)

if c-a < 0:
    numList.append(-(c-a))
else:
    numList.append(c-a)

if b - d < 0:
    numList.append(-(b - d))
else:
    numList.append(b - d)
if d - b < 0:
    numList.append(-(d - b))
else:
    numList.append(d - b)

print(min(numList))