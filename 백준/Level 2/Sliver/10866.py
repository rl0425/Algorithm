num = int(input())

dequeue = []
answer = []

for x in range(num):
    ans = list(input().split())
    if len(ans) > 1:
        if ans[0] == "push_front":
            dequeue.insert(0, ans[1])

        if ans[0] == "push_back":
            dequeue.append(ans[1])

    if ans[0] == "front":
        if len(dequeue) > 0:
            answer.append(dequeue[0])
        else:
            answer.append(-1)

    if ans[0] == "back":
        if len(dequeue) > 0:
            answer.append(dequeue[len(dequeue)-1])
        else:
            answer.append(-1)

    if ans[0] == "empty":
        if len(dequeue) > 0:
            answer.append(0)
        else:
            answer.append(1)

    if ans[0] == "size":
        answer.append(len(dequeue))

    if ans[0] == "pop_front":
        if len(dequeue) > 0:
            answer.append(dequeue.pop(0))
        else:
            answer.append(-1)

    if ans[0] == "pop_back":
        if len(dequeue) > 0:
            answer.append(dequeue.pop())
        else:
            answer.append(-1)

print(*answer)