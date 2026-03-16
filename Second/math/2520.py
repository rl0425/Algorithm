sumIsu = 0
sumSco = 0

dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

for _ in range(20):
    s, h, g = list(map(str, input().split()))

    if g == 'P':
        continue
    sumIsu += float(h)
    sumSco += float(h) * dict[g]

print(sumSco/sumIsu)


