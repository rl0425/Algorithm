import sys
input = sys.stdin.readline

m, n = map(int, input().split())
password = dict()

for _ in range(m):
    key, value = input().rstrip().split()

    # 사이트 key, value 저장
    password[key] = value

for _ in range(n):
    key = input().rstrip()

    # 패스워드 가져오기
    print(password[key])
