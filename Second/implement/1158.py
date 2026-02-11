n, k = map(int, input().split())

arr = [i + 1 for i in range(n)]
now = 0
answer = []

while arr:
    now = (now + (k - 1)) % len(arr)
    answer.append(arr.pop(now))

print(f"<{', '.join(map(str, answer))}>")