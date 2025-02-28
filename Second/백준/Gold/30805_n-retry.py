import itertools

n = int(input())
n_arr = ''.join(list(map(str, input().split())))
m = int(input())
m_arr = ''.join(list(map(str, input().split())))

cal_arr = []
ans_arr = []

for i in range(1, n+1):
    temp = list(itertools.combinations(n_arr, i))
    for item in temp:
        cal_arr.append(''.join(list(item)))

for item in cal_arr:
    index = 0
    default_index = 0
    while True:
        if default_index == m or default_index >= len(item):
            break
        is_find = m_arr.find(item[index], default_index, m)

        if is_find != -1:
            index += 1
        default_index += 1

    if index == len(item):
        ans_arr.append(item)

last_num = sorted(ans_arr, key=str.lower)[-1]

print(len(last_num))
print(*last_num)