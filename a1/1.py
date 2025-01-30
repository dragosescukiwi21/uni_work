def suma(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10

    return s

n = int(input())

while n > 9:
    n = suma(n)

print(n)