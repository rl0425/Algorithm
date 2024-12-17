import sys
sys.setrecursionlimit(100000)

G = int(input())
P = int(input())

gate = {i:i for i in range(G+1)}
plane = []

for _ in range(P):
    plane.append(int(sys.stdin.readline()))

def find(num):
    if gate[num] == num:
        return num

    gate[num] = find(gate[num])
    return gate[num]

cnt = 0

for i in plane:
    tmp = find(i)
    if tmp == 0:
        break

    gate[tmp] = tmp - 1
    cnt += 1

print(cnt)