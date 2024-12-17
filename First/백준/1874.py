a = int(input())
arrays = []

for x in range(a):
    arrays.append(int(input()))

stack = []
answer = []
count = 0

for x in arrays:
    if count > a:
        break

    if count >= x:
        num = stack.pop()

        if num != x:
            answer.append("0")
            break

        else:
            answer.append("-")
    else:
        while True:
            count += 1
            stack.append(count)
            answer.append("+")

            if count >= x:
                num = stack.pop()
                if num != x:
                    answer.append("0")
                    break

                else:
                    answer.append("-")
                    break


if "0" in answer:
    print("NO")
else:
    print(*answer)