a = int(input())

inputData = []

for x in range(a):
    inputData.append(int(input()))

score = inputData[len(inputData)-1]
index = len(inputData)-1
combo = False

if len(inputData) == 1:
    print(inputData[0])

elif len(inputData) == 2:
    print(inputData[0]+inputData[1])
else:
    while True:
        if index == 1:
            score += inputData[index-1]
            break

        if index == 2:
            if combo:
                score += inputData[index-2]
                break
            else:
                if inputData[index - 1] > inputData[index - 2]:
                    score += inputData[index-1]
                    break
                else:
                    score += inputData[index-2]
                    break
        else:
            if combo:
                index -= 2
                score += inputData[index]
                combo = False
            else:
                if inputData[index-1] >= inputData[index-2]:
                    index -= 1
                    score += inputData[index]
                    combo = True
                else:
                    index -= 2
                    score += inputData[index]
                    combo = False

        print("score = ", score)

    print(score)
