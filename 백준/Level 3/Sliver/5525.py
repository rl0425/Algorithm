a = int(input())
b = int(input())
c = input()

count = 0
answer = 0
index = 1

while index < b-1:
    if c[index-1] == "I" and c[index] == "O" and c[index+1] == "I":
        count += 1
        if count == a:
            count -= 1
            answer += 1
        index += 1
    else:
        count = 0
    index += 1

print(answer)


# 50점 답안
# x = "IOI"
# count = 0
#
# if a == 1:
#     x = "IOI"
# else:
#     for ele in range(a-1):
#         x += "OI"
#
# for ele in range(b):
#     if x in c[ele:len(x)+ele]:
#         count += 1
#
# print(count)

