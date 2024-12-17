import sys
input = sys.stdin.readline

a = int(input())
inputData = set()

for x in range(a):
    temp = list(map(str, input().rstrip().split()))

    if temp[0] == "add":
        inputData.add(int(temp[1]))
    if temp[0] == "remove":
        if int(temp[1]) in inputData:
            inputData.remove(int(temp[1]))
    if temp[0] == "check":
        if int(temp[1]) in inputData:
            print("1")
        else:
            print("0")
    if temp[0] == "toggle":
        if int(temp[1]) in inputData:
            inputData.remove(int(temp[1]))
        else:
            inputData.add(int(temp[1]))
    if temp[0] == "all":
        inputData = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    if temp[0] == "empty":
        inputData.clear()
