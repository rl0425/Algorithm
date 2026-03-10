n = int(input())
ans = 99

if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        hansu = True
        for j in range(len(str(i))-2):
            if int(str(i)[j]) - int(str(i)[j+1]) != int(str(i)[j+1]) - int(str(i)[j+2]):
                hansu = False
                break
        if hansu:
            ans += 1

    print(ans)



