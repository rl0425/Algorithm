import sys
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))
lis = [0]

for case in cases:
    if lis[-1]<case:
        lis.append(case)
        print("case = ", case)
        print("lis = ", lis)

    else:
        left = 0
        right = len(lis)

        while left<right:
            mid = (right+left)//2
            if lis[mid]<case:
                left = mid+1
            else:
                right = mid
        lis[right] = case
        print("list[right] =", case)
        print("right =", right)


print(len(lis)-1)
print(lis)

# 10
# 100 50 70 90 75 87 105 78 110 60

# 100, 50, 70, 90, 75, 87, 105, 78, 110, 60