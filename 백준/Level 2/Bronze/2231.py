a = int(input())
count = 1
type = False

while True:
    if a == 1:
        type = False
        break

    hap = count
    for x in str(count):
        hap += int(x)

    if hap == a:
        type = True
        print(count)
        break

    count += 1

    if count == a:
        break

if type == False:
    print(0)