a, b = map(int, input().split())

flag = [0 for _ in range(100001)]

def bfs(start):
    array = []
    array.append(start)

    while len(array) != 0:
        num = int(array.pop(0))

        if num == b:
            return flag[num]

        list = []

        if num - 1 >= 0:
            list.append(num-1)
        if num + 1 <= 100000:
            list.append(num+1)
        if num * 2 <= 100000:
            list.append(num*2)

        for x in list:
            if flag[x] == 0:
                array.append(x)
                flag[x] = flag[num] + 1

print(bfs(a))


