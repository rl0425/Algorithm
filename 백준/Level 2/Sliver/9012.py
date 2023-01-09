a = int(input())

stack = []
answer = []
last = ""

for x in range(a):
    data = input()

    for y in range(len(data)):
        if data[y] == "(":
            stack.append("(")
            last = "("

        elif data[y] == ")":
            if y > 0 and last == "(":
                stack.pop()

                if len(stack) > 0:
                    last = stack[len(stack)-1]
                else:
                    last = ""
            else:
                stack.append(")")
                last = ")"

    if len(stack) > 0:
        answer.append("NO")
    else:
        answer.append("YES")

    stack = []

print(*answer)

