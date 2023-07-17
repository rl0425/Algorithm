from itertools import combinations

# 문제 개수
count = int(input())

for _ in range(count):
    # 문자열 개수
    x = int(input())

    # 문자열 리스트
    case = input().split()

    if x >= 33:
        print(0)

    else:
        # 문자열 리스트 조합
        combi = list(combinations(case, 3))

        # 최대 수
        answer = 100000

        for x in combi:
            temp = 0
            # 세 개의 문자열의 조합
            for str1, str2 in combinations(x, 2):
                # 각 문자열의 문자들을 하나씩 비교
                for char1, char2 in zip(str1, str2):
                    # 문자가 틀릴 경우 숫자 증가
                    if char1 != char2:
                        temp += 1

            # 가장 작은 수
            if answer > temp:
                answer = temp

        print(answer)