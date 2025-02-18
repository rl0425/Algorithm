import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def getPreorder(inorder, postorder, in_start, in_end, post_start, post_end, position):
    if in_start > in_end:
        return []

    root = postorder[post_end]
    mid = position[root]

    left_size = mid - in_start

    return [root] + \
        getPreorder(inorder, postorder, in_start, mid - 1, post_start, post_start + left_size - 1, position) + \
        getPreorder(inorder, postorder, mid + 1, in_end, post_start + left_size, post_end - 1, position)

# 메인 코드
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 인오더에서의 각 값의 위치를 미리 저장
position = {val: idx for idx, val in enumerate(inorder)}

result = getPreorder(inorder, postorder, 0, n - 1, 0, n - 1, position)
print(*result)