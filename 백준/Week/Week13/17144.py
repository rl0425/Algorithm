r, c, t = map(int,input().split())

arr = [[] for _ in range(r)]

conditional = [-1, -1]

def rotate():
    global arr

    temp = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if arr[x][y] != 0:
                cnt = 0
                if x-1 >= 0 and arr[x-1][y] != -1:
                    cnt += 1

                    temp[x-1][y] = temp[x-1][y] + int(arr[x][y] / 5)
                if x+1 < r and arr[x+1][y] != -1:
                    cnt += 1

                    temp[x+1][y] = temp[x+1][y] + int(arr[x][y] / 5)
                if y-1 >= 0 and arr[x][y-1] != -1:
                    cnt += 1

                    temp[x][y-1] = temp[x][y-1] + int(arr[x][y] / 5)
                if y+1 < c and arr[x][y+1] != -1:
                    cnt += 1

                    temp[x][y+1] = temp[x][y+1] + int(arr[x][y] / 5)


                temp[x][y] = temp[x][y] + arr[x][y] - int(arr[x][y]/5) * cnt

                # print("Tem = ", temp)
    # 역방향
    for x in range(conditional[0]-1, 0, -1):
        temp[x][0] = temp[x-1][0]
    for y in range(0, c-1):
        temp[0][y] = temp[0][y+1]
    for x in range(0, conditional[0]):
        temp[x][c-1] = temp[x+1][c-1]
    for y in range(c-1, 0, -1):
        temp[conditional[0]][y] = temp[conditional[0]][y-1]

        if temp[conditional[0]][y] == -1:
            temp[conditional[0]][y] = 0

#   정방향
    for x in range(conditional[1]+1, r-1):
        temp[x][0] = temp[x+1][0]
    for y in range(0, c-1):
        temp[r-1][y] = temp[r-1][y+1]
    for x in range(r-1, conditional[1], -1):
        temp[x][c-1] = temp[x-1][c-1]
    for y in range(c-1, 0, -1):
        temp[conditional[1]][y] = temp[conditional[1]][y - 1]

        if temp[conditional[1]][y] == -1:
            temp[conditional[1]][y] = 0

    arr = temp


for i in range(r):
    arr[i] = [int(x) for x in input().split()]

    for j in range(c):
        if arr[i][j] == -1 and conditional[0] != -1:
            conditional[1] = i
        if arr[i][j] == -1 and conditional[0] == -1:
            conditional[0] = i

for _ in range(t):
    rotate()

sum = 0

for x in range(r):
    for y in range(c):
        if arr[x][y] != -1 and arr[x][y] != 0:
            sum += arr[x][y]

print(sum)