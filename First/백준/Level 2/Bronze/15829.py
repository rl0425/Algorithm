from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)

num = int(input())

inputData = input()
hap = 0

for x in range(num):
    index = alphabet_list.index(inputData[x])+1 % 1234567891
    modIndex = 1
    for y in range(x):
        modIndex = (modIndex * 31) % 1234567891

    hap += (index * modIndex) % 1234567891
    hap = hap % 1234567891

print(hap)