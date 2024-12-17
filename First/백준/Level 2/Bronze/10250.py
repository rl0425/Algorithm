num = int(input())
answer = []

for x in range(num):
    a,b,c = map(int,input().split())
    bang = 0

    if c % a != 0:
        bang = ((c % a) * 100) + (c//a + 1)
    else:
        bang = (a * 100) + (c // a)

    answer.append(bang)

print(*answer)