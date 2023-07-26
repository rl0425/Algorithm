a, b, c = map(int, input().split())

def power(C, n):
    result = 1
    while n:
        if n % 2 != 0:
            result *= C
        C *= C
        n //= 2
    return result


print(power(a, b) % c)