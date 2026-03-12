def find_fraction():
    try:
        X = int(input())
    except EOFError:
        return

    line = 1
    # 1. X가 몇 번째 라인에 있는지 찾기
    while X > line:
        X -= line
        line += 1

    # 이제 line은 해당 대각선 번호, 
    # X는 그 라인 내에서의 순서가 됩니다.

    if line % 2 == 0:
        # 짝수 라인: 분자 증가, 분모 감소 (위 -> 아래)
        numerator = X
        denominator = line - X + 1
    else:
        # 홀수 라인: 분자 감소, 분모 증가 (아래 -> 위)
        numerator = line - X + 1
        denominator = X

    print(f"{numerator}/{denominator}")


find_fraction()