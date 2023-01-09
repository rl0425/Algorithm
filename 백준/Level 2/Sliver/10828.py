num = int(input())

stack = []
answer = []

for x in range(num):
    ans = list(input().split())
    if len(ans) > 1:
        stack.append(ans[1])

    if ans[0] == "top":
        if len(stack) > 0:
            answer.append(stack[len(stack)-1])
        else:
            answer.append(-1)

    if ans[0] == "empty":
        if len(stack) > 0:
            answer.append(0)
        else:
            answer.append(1)

    if ans[0] == "size":
        answer.append(len(stack))

    if ans[0] == "pop":
        if len(stack) > 0:
            answer.append(stack.pop())
        else:
            answer.append(-1)

print(*answer)