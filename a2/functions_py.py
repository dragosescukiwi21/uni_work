def add(list, value):
    # adding the value to the end of the list

    list.append(value)
    return list


def my_remove(list, index):
    # removing the value at index "index"

    list.remove(list[index])
    return list


def insert(list, index, value):
    # inserting value at index "index"

    list.insert(index, value)
    return list


def remove2(list, from_index, to_index):
    # removing the element at the starting index (the other x elements will fall in this position
    # after popping them) until the length of this sequence

    x = abs(from_index - to_index)
    for e in range(x):
        list.pop(from_index)

    return list


def replace(list, old_value, new_value):
    n = len(old_value)

    i = 0
    # here we check every sequence in the list of length old_value, reason why
    # we only check until len(list) - n so that we don't go out of bound

    while i <= len(list) - n:

        # we check for subsequences of length old_value and in case we find one,
        # we replace it

        if list[i:i + n] == old_value:
            list[i:i + n] = new_value

            # skip the valid sequence
            i += len(new_value)

        else:
            # we find a new value of len old_value that we can replace
            i += 1

    return list


def odd(list, st, dr):
    odd_list = []

    # checking for odd elements in list between index st and dr and adding them to counter "c"
    for i in range(st, dr):
        if list[i] % 2 == 1:
            odd_list.append(list[i])

    return odd_list

def suma(list, st, dr):
    s = 0

    # adding each element in list between index st and dr to the sum
    for i in range(st, dr):
        s += list[i]

    return s


def gcd(a, b):
    # doing the classic Euclidean algorithm 2 elements a, b
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def gcd_make(list, st, dr):
    # successively gcd-ing 2 elements from the list so that we cover all dr - st + 1 elements
    for i in range(st, dr ):
        list[i + 1] = gcd(list[i], list[i + 1])

    # gcd of all these elements will fall right on list[dr]
    return list[dr]


def maxi(list, st, dr):
    # classic max algo

    mxa = list[st]
    for i in range(st, dr):
        if list[i] > mxa:
            mxa = list[i]

    return mxa


def isPrime(n):
    # classic prime algo
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False

        i += 2
        
    return True


def prime(list, st, dr):
    prime_list = []

    # if we find a prime between st, dr we put it at the end of the list
    for i in range(st, dr):
        if isPrime(list[i]):
            prime_list.append(list[i])

    return prime_list

def filter_primes(list):
    i = 0
    # Only iterating through the list if we're not removing an element from the list.
    # Otherwise, we would end up iterating too many times and going out of bound
    
    while i < len(list):
        if not isPrime(list[i]):
            list.pop(i)
        else:
            i += 1

    return list

def filter_negatives(list):
    i = 0
    # Same as for filter_prime but removing the positive numbers
    
    while i < len(list):
        if list[i] >= 0:
            list.pop(i)
        else:
            i += 1

    return list