import sys

input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

nameData = {}
numData = {}

for x in range(a):
    value = input().rstrip()

    nameData[value] = x+1
    numData[str(x+1)] = value

for x in range(b):
    value = input().rstrip()

    if value.isdigit():
        print(numData[value])
    else :
        print(nameData[value])
