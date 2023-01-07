a,b = map(int,input().split())

list = list(map(int,input().split()))
list.sort(reverse=True)

end = False
answer = []

for x in range(len(list)-2):
    for y in range(x+1,len(list)-1):
        for z in range(y+1,len(list)):
            if list[x]+list[y]+list[z] <= b:
                answer.append(list[x]+list[y]+list[z])

print(max(answer))