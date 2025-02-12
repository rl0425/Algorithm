n = int(input())
s = list(map(int, input().split()))

answer = 0
left = 0
count = [0] * 10  # 각 숫자의 등장 횟수를 저장
distinct = 0  # 현재 구간에서 서로 다른 숫자의 개수

for right in range(n):
    # 새로운 숫자가 추가될 때
    if count[s[right]] == 0:
        distinct += 1
    count[s[right]] += 1

    # 서로 다른 숫자가 3개 이상이면 left를 이동
    while distinct > 2:
        count[s[left]] -= 1
        if count[s[left]] == 0:
            distinct -= 1
        left += 1

    # 현재 구간의 길이와 최대 길이 비교
    answer = max(answer, right - left + 1)

print(answer)