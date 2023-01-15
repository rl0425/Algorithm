a, b = map(int, input().split())

count = 0

def basuFunc(num):
    basu = 2
    while True:
        if num < basu:
            basu = int(basu / 2)
            break
        else:
            basu = basu * 2

    return basu

numList = []

while True:
    if(a <= 2):
        if a != 0:
            numList.append(a)
        break

    else:
        value = basuFunc(a)
        numList.append(value)
        a = a - value

while len(numList) > b:
    low = numList.pop()
    high = numList.pop()

    count += high - low
    numList.append(high*2)

print(count)

# 40~50분 소요