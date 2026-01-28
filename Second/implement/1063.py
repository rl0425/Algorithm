k, s, n = map(str, input().split())

rules = {
    'R': (1, 0),
    'L':  (-1,0),
    'B': (0, 1),
    'T': (0, -1),
    'RT': (1, -1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (-1, 1),
}

king = ((ord(k[0]) - ord('A')), (8-int(k[1])))
stone = ((ord(s[0]) - ord('A')), (8-int(s[1])))

for _ in range(int(n)):
    key = str(input())

    dx, dy = rules[key][0], rules[key][1]

    if 0 <= dx + king[0] < 8 and 0 <= dy + king[1] < 8:
        nx, ny = ((king[0] + dx), (king[1] + dy))
        if (nx, ny) == stone:
            sx, sy = ((stone[0] + dx), (stone[1] + dy))
            if 0 <= sx < 8 and 0 <= sy < 8:
                king = (nx, ny)
                stone = (sx, sy)
            else:
                continue
        else:
            king = (nx, ny)

print(chr(ord('A') + king[0]) + str(8 - king[1]))
print(chr(ord('A') + stone[0]) + str(8 - stone[1]))
