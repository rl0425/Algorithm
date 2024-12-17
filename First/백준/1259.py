list = []
answer = []

while True:
    a = input()
    if a == str(0):
        break
    else:
        list.append(a)

for x in list:
    count = 0
    type = "odd"

    if len(x) // 2 == 0:
        type = "even"

    while True:
        if len(x) == 1:
            print("yes")
            break

        if type == "odd" and count == len(x) // 2:
            print("yes")
            # answer.append("yes")
            break

        if x[0+count] != x[len(x)-1 - count]:
            print("no")
            # answer.append("no")
            break

        if type == "even" and count == (len(x) // 2) - 1:
            print("yes")
            # answer.append("yes")
            break

        count += 1


