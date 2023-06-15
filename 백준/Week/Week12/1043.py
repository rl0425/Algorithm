a, b = map(int, input().split())
truth = list(map(int, input().split()))
del truth[0]

partyList = []
passArr = []

num = 0
index = 0

for x in range(b):
    party = list(map(int,input().split()))
    del party[0]
    partyList.append(party)

while True:
    if index >= len(partyList):
        break

    has_common_element = any(item in partyList[index] for item in truth)

    if has_common_element:
        for y in range(len(partyList[index])):
            truth.append(partyList[index][y])

        passArr.append(index)
        index = 0

        while True:
            if index not in passArr:
                break
            index += 1

    else:
        while True:
            index += 1
            if index not in passArr:
                break

for x in range(len(partyList)):
    has_common_element = any(item in partyList[x] for item in truth)

    if has_common_element == False:
        num += 1

print(num)