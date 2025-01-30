# we calculate suma gauss of n
def sg(n):
    return n * (n + 1) // 2


k = int(input())
found = False

i = 1

# finding in which subsequence the postion k is found
while not found:
    if sg(i - 1) <= k <= sg(i):
        found = True
        print(i)

    i += 1
