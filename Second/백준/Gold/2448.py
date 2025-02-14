def draw_stars(n):
    # 기본 별 패턴
    base = ['  *  ', ' * * ', '*****']

    print("base = ", base)

    # 현재 높이
    k = 3
    while k < n:
        # 이전 패턴을 복사
        temp = base[:]

        print("temp =", temp)

        # 아래쪽에 이전 패턴을 두 번 복사
        for i in range(len(temp)):
            # 왼쪽 패턴
            base.append(temp[i] + ' ' + temp[i])

        # 위쪽에 공백 추가
        # for i in range(k):
        #     base[i] = ' ' * k + base[i] + ' ' * k
        print("k = ", k)
        k *= 2


    # 결과 출력
    print('\n'.join(base))


# 입력 받기
n = int(input())
draw_stars(n)