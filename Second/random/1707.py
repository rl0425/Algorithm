import sys

k = int(input())
input = sys.stdin.readline

def DFS(dict, vtype, sorted_keys):
    arr = sorted_keys
    isValid = True

    while arr:
        d1 = arr.pop()
        if vtype[d1] != 'a' and vtype[d1] != 'b':
            vtype[d1] = 'a'

        if d1 in dict:
            if visited[d1] > 2:
                continue
            visited[d1] += 1
            for e in dict[d1]:

                # print("vtype =", vtype)
                # print("d1 = ", d1)
                # print("e = ", e)
                # print("====")

                if vtype[d1] == 'a':
                    if vtype[e] == 'a':
                        isValid = False
                        break
                    else:
                        vtype[e] = 'b'
                        arr.append(e)
                if vtype[d1] == 'b':
                    if vtype[e] == 'b':
                        isValid = False
                        break
                    else:
                        vtype[e] = 'a'
                        arr.append(e)
            if not isValid:
                break

    return isValid

for _ in range(k):
    v, e = map(int, input().split())

    vtype = ['c' for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    dict = {}
    isValid = True

    for _ in range(e):
        u, v = map(int, input().split())
        if u not in dict:
            dict[u] = [v]
        else:
            dict[u].append(v)

        if v not in dict:
            dict[v] = [u]
        else:
            dict[v].append(u)

    isValid = DFS(dict, vtype, list(dict.keys()))

    print('YES' if isValid else 'NO')

