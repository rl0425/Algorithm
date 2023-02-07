a, b = map(int, input().split())

answer = 0

chae = [False, False] + [True]*(b-1)
primes=[]
def soinsu(x):
    d = 2
    length = 0
    sosu = True

    while d <= x:
        if x % d == 0:
            x = x / d
            length += 1
        else:
            d += 1

    if length == 0 or length == 1:
        sosu = False

    elif length == 2:
        sosu = True

    else:
        if chae[length]:
            sosu = True
        else:
            sosu = False

    return sosu

for i in range(2,int(b**0.5)+1):
  if chae[i]:
    # primes.append(i)
    for j in range(2*i, b+1, i):
        chae[j] = False

# print(primes)

for x in range(a, b+1):
    if soinsu(x):
        answer += 1

print(answer)

