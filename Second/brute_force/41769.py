arr = [0] * 10001

for i in range(1, 10001):
    sum = i
    for c in str(i):
        sum += int(c)

    if sum < 10001:
        arr[sum] = 1

for i in range(1, len(arr)):
    if arr[i] == 0:
        print(i)

