n, m = map(int, input().split())

sixMin = 1000
divideMin = 1000

for _ in range(m):
    dx, dy = map(int, input().split())

    if dx <= sixMin:
        sixMin = dx
    if dy <= divideMin:
        divideMin = dy

if sixMin >= divideMin * 6:
    print(n * divideMin)
else:
    answer = min((n // 6) * sixMin + (n % 6) * divideMin, ((n // 6) + 1) * sixMin)
    print(answer)
