# here I will determine if the first element (from r to l)
# is at an odd position or an even position

def odd_even(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10

    return c % 2


n = int(input())
x = odd_even(n)

num = 0
p = 1

# constructing the number for each odd position
while n > 0:
    num += (n % 10) * x * p

    n //= 10
    x = (x + 1) % 2

    if x % 2 == 0:
        p *= 10

print(num)