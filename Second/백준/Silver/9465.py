n = int(input())

for _ in range(n):
    cnt = int(input())
    answer = 0
    arr = []

    for x in range(2):
        arr.append(list(map(int, input().split())))
    for x in range(cnt):
        for y in range(2):
            max_list = [0]
            if y == 0:
                if x-1 >= 0:
                    max_list.append(arr[1][x-1])
                if x-2 >= 0:
                    max_list.append(arr[0][x-2])
                    max_list.append(arr[1][x-2])
            if y == 1:
                if x-1 >= 0:
                    max_list.append(arr[0][x-1])
                if x-2 >= 0:
                    max_list.append(arr[0][x - 2])
                    max_list.append(arr[1][x - 2])

            arr[y][x] += max(max_list)
            answer = max(answer, arr[y][x])
    print(answer)
