a,b = map(int, input().split())
answer = []

def sosu(val):
    value = True

    for y in range(2, int(val ** 0.5)+1):
        if val % y == 0:
            value = False
            break

    if val == 1:
        value = False

    if value:
        print(int(val))


for x in range(a, b+1):
    sosu(x)

