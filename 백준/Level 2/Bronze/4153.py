answer = []

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    else:
        case = sorted([a, b, c])
        if (case[0]*case[0] + case[1]*case[1] == case[2]*case[2]):
            answer.append("right")
        else:
            answer.append("wrong")

print(*answer)