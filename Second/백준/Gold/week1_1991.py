from collections import deque
from copy import deepcopy


def preorder(set):
    queue = deque()
    queue.append('A')
    answer = ''

    while len(queue):
        now = queue.popleft()
        answer += now

        if set[now][1] != '.':
            queue.appendleft(set[now][1])
        if set[now][0] != '.':
            queue.appendleft(set[now][0])

    print(answer)

def inorder(set):
    nowSet = deepcopy(set)
    queue = deque()
    queue.append('A')
    answer = ''
    while len(queue):
        now = queue.popleft()

        if nowSet[now][0] != '.':
            queue.appendleft(now)
            queue.appendleft(nowSet[now][0])
            continue

        if nowSet[now][0] == '.':
            answer += now
            if len(queue) != 0:
                nowSet[queue[0]][0] = '.'

        if nowSet[now][1] != '.':
            queue.appendleft(nowSet[now][1])

    print(answer)

def postorder(set):
    nowSet = deepcopy(set)
    queue = deque()
    queue.append('A')
    answer = ''

    while len(queue):
        now = queue[0]
        leftNode = nowSet[now][0]
        rightNode = nowSet[now][1]

        if rightNode != '.' and rightNode not in answer:
            queue.appendleft(rightNode)
        if leftNode != '.' and leftNode not in answer:
            queue.appendleft(leftNode)

        if leftNode == '.' or leftNode in answer:
            if rightNode == '.' or rightNode in answer:
                answer += now
                queue.popleft()

    print(answer)

n = int(input())
nodeSet = {}

for _ in range(n):
    line = input().split()
    parent = line[0]
    childSet = line[1:]

    if parent not in nodeSet:
        nodeSet[parent] = []

    for child in childSet:
        nodeSet[parent].append(child)

preorder(nodeSet)
inorder(nodeSet)
postorder(nodeSet)

# 1h 30min