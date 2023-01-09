num = int(input())

zero = 0
one = 0

def fibonacci(n):
    print("n = ", n)

    if n == 1:
        print("1")
        return 1
    elif n == 0:
        print("2")
        return 0
    else:
        print("3")
        a = fibonacci(n-1)
        print("a =", a)
        b = fibonacci(n-2)
        print("b = ", b)
        d = a + b
        print("d = ", d)

for x in range(num):
    print(fibonacci(int(input())))
    
