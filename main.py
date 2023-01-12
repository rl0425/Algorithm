# 자주 쓰인다 / 입력값 두개
#a, b = map(int, input().split())
#a = int(input())
#print(a-b)

# 여러개 입력

# n = int(input())
# inputData = []
#
# for x in range(n):
#     c = input()
#     inputData.append(c)
#
# print(inputData)

# 조건문
# if a <= 100 and a >= 90:
#     print("A")
# elif a < 90 and a >= 80:
#     print("B")
# elif a < 80 and a >= 70:
#     print("C")
# elif a < 70 and a >= 60:
#     print("D")
# else:
#     print("F")

# 반복문
# for x in a:
#     print(x)
#

# print 반복문
# a = [1,2]
# print(a*100)

# while a > 100:
#  print("1")
#  a+= 1

# for x in range(a):
#     x += 1
#     for y in range(x):
#         print("*", end="")
#     print("")

# a = int(input())
# b = 0
# while True:
#     b += 1
#     if b > a:
#         break;
#     else:
#         print("*" * b)

# a = [1,2,3,4,5]
#
# a.insert(0, 6)
# a.append(3)
#
# a.pop()
# c = a.pop(0)
#
# b = sorted(a)
# b.reverse()
#
# # 첫 인덱스 앞에서 뒷 인덱스 앞을 자른다
# print(a[1:3])
# # 전체
# print(a[:])
# # 세 번째 인자 , 몇 개씩 뛰어 넘을지
# print(a[1:5:2])
# # 역순
# print(a[::-1])
#
# # range도 범위지정이 가능하다, 세번째 인덱스는 몇 개를 뛰어넘을지
# for x in range(0,100, 2):
#     print(x)
#
# # dictionary , key/value
# ab = dict()
# abc = {}
#
# a["1"] = 1
# a["2"] = 2
# a["3"] = 3
#
# # 키가 있는지 홗인하는 방법
# print("5" in a)
#
# # key를 하나씩 뺀다
# for x in a.keys():
#     print(a[x])
#
# # set, 중복 제거 시 사용한다
# a = set()
# b = set()
#
# # 합집합 = union , 차집합 difference
# a.add(a)
# b.add(2)
#
# c = a.union(b)
# print(a)

# n = int(input())
# inputData = []
#
# for x in range(n):
#     c = input()
#     inputData.append(c)
#
# a = 0
# answerData = []
# for x in inputData:
#     b = 0
#     for y in range(len(x)):
#         if x[y] == "O":
#             a += 1
#             b += a
#         else:
#             a = 0
#     a = 0
#     answerData.append(b)
#
# print(*answerData)


a, b = map(int, input().split())

inputData = []

for x in range(a):
    c = input()
    inputData.append(int(c))

maxValue = max(inputData)
valueSum = 0

while True:
    for x in inputData:
        valueSum += x // maxValue

    if valueSum != b:
        if valueSum > b:
            if valueSum // 2 < b:
                maxValue = maxValue * 2
            elif valueSum < b:
                print("Hhh")
                maxValue = maxValue + 1
        elif valueSum < b:
            if valueSum * 2 < b:
                maxValue = maxValue // 2
            elif valueSum < b:
                print("ccc")
                maxValue = maxValue - 1

        valueSum = 0

    if valueSum == b:
        print(maxValue)
        break