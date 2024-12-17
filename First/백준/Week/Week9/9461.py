inputData = []
p = [0 for _ in range(100)]

p[0] = 1
p[1] = 1
p[2] = 1
p[3] = 2

for x in range(4, 100):
    p[x] = p[x-1] + p[x-5]

for x in range(int(input())):
    print(p[int(input()) -1])