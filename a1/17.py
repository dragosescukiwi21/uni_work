def suma(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10

    return s


n = int(input())
ref_n = n

found = False

while not found:
    if ref_n + suma(ref_n) == n:
        found = True
        print(ref_n)

    ref_n -= 1
