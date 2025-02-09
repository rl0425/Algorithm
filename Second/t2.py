def solution(edges):
    answer = []
    lines = {}

    answer.remove(1)

    for a, b in edges:
        if a not in lines:
            lines[a] = set()
        lines[a].add(b)

    for start in lines:
        for child in lines[start]:
            lines[start].remove(child)
            while True:
                child


    print(lines)
    return answer


edges = [[2, 3], [4, 3], [1, 1], [2, 1]]

solution(edges)