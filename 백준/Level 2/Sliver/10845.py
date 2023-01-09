num = int(input())

queue = []
answer = []

for x in range(num):
    ans = list(input().split())
    if len(ans) > 1:
        queue.append(ans[1])

    if ans[0] == "front":
        if len(queue) > 0:
            answer.append(queue[0])
        else:
            answer.append(-1)

    if ans[0] == "back":
        if len(queue) > 0:
            answer.append(queue[len(queue)-1])
        else:
            answer.append(-1)

    if ans[0] == "empty":
        if len(queue) > 0:
            answer.append(0)
        else:
            answer.append(1)

    if ans[0] == "size":
        answer.append(len(queue))

    if ans[0] == "pop":
        if len(queue) > 0:
            answer.append(queue.pop(0))
        else:
            answer.append(-1)

print(*answer)