def fibo(num):
    num_arr = []
    fibo_len = len(fibonacci) -1

    while num != 0:
        if fibonacci[fibo_len] > num:
            fibo_len -= 1
        if fibonacci[fibo_len] <= num:
            num -= fibonacci[fibo_len]
            num_arr.append(fibonacci[fibo_len])
            if fibonacci[fibo_len] > 1:
                fibo_len -= 1
    return num_arr


a, b = 0, 1
fibonacci = [a, b]
while True:
    a, b = b, a+b
    if b >= 1000000000:
        break
    fibonacci.append(a+b)

n = int(input())

for _ in range(n):
    num = int(input())
    arr = reversed(fibo(num))
    print(*arr)
