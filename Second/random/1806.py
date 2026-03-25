n, s = map(int, input().split())
nlist = list(map(int, input().split()))

start = 0
end = 1
sum = nlist[0] + nlist[1]

min = float('inf')

if nlist[0] >= s:
    print("1")

else:
    while start <= end:
        if sum < s:
            if end + 1 >= len(nlist):
                break
            end += 1
            sum += nlist[end]
        elif sum >= s:
            if min > end - start + 1:
                min = end - start + 1
            sum -= nlist[start]
            start += 1

    print(min if min != float('inf') else 0)

