a, b, c = map(int, input().split())

d = ((c-a) // (a-b))
nad = (c-a) % (a-b)

if nad != 0:
    d += 1

if d == 0:
    d += 1

if a == c:
    d = 0

print(d+1)