import functions_py

def options(lst, q):
    if q == "1": # Add function
        assert functions_py.add([7, 4, -2, 8], 8) == [7, 4, -2, 8, 8]
        assert functions_py.add([1, 2], -5) == [1, 2, -5]
        assert functions_py.add([10, 10, 10, 10, 9], 8) == [10, 10, 10, 10, 9, 8]
        assert functions_py.add([1, 2, 3, 4], 5) == [1, 2, 3, 4, 5]
        assert functions_py.add([], 8) == [8]

        val = int(input("Enter a value you would like to add: "))
        functions_py.add(lst, val)

        print(lst, end='\n')

    if q == "2":  # Insert function
        assert functions_py.insert([5, 2, 8], 1, 99) == [5, 99, 2, 8]
        assert functions_py.insert([10, 20], 2, 30) == [10, 20, 30]
        assert functions_py.insert([1, 1, 1], 0, 0) == [0, 1, 1, 1]
        assert functions_py.insert([3, 5, 7], 3, 9) == [3, 5, 7, 9]
        assert functions_py.insert([], 0, 10) == [10]

        idx = int(input("Enter the index where you want to insert: "))
        val = int(input("Enter the value you want to insert: "))

        functions_py.insert(lst, idx, val)
        print(lst, end='\n')


    if q == "3": # Remove function
        assert functions_py.my_remove([7, 4, -2, 8], 2) == [7, 4, 8]
        assert functions_py.my_remove([1, 2], 0) == [2]
        assert functions_py.my_remove([10, 10, 10, 10, 9], 4) == [10, 10, 10, 10]
        assert functions_py.my_remove([1, 2, 3, 4], 1) == [1, 3, 4]
        assert functions_py.my_remove([7], 0) == []

        i = int(input("Enter the index of the value you would like to remove: "))
        functions_py.my_remove(lst, i)

        print(lst, end='\n')


    if q == "4":  # Remove (from i to j)
        assert functions_py.remove2([7, 4, -2, 8, 9], 1, 3) == [7, 8, 9]
        assert functions_py.remove2([0, 1, 2, 3, 4], 0, 2) == [2, 3, 4]
        assert functions_py.remove2([100, 200, 300, 400], 1, 2) == [100, 300, 400]
        assert functions_py.remove2([10, 20, 30, 40], 0, 1) == [20, 30, 40]
        assert functions_py.remove2([1, 2, 3, 4, 5], 2, 4) == [1, 2, 5]

        i = int(input("Enter the starting index to remove: "))
        j = int(input("Enter the ending index to remove: "))

        functions_py.remove2(lst, i, j)

        print(lst, end='\n')

    if q == "5":  # Replace function
        assert functions_py.replace([9, 7, 5, 3], [7, 5], []) == [9, 3]
        assert functions_py.replace([1, 1, 2, 3], [6, 3, 9], [1, 2]) == [1, 1, 2, 3]
        assert functions_py.replace([8, 8, 9, 2, 4], [8, 8, 9], [10000, 150]) == [10000, 150, 2, 4]
        assert functions_py.replace([50, 60, 70], [50, 60], [0]) == [0, 70]
        assert functions_py.replace([1, 2, 3, 4], [4], [549, 400, 90, 739]) == [1, 2, 3, 549, 400, 90, 739]

        old_val = int(input("Enter the sublist you want to replace: "))
        new_val = int(input("Enter a list you want to introduce: "))

        functions_py.replace(lst, old_val, new_val)

        print(lst, end='\n')

    if q == "6":  # Prime function
        assert functions_py.prime([11, 12, 13, 14], 1, 3) == [13]
        assert functions_py.prime([4, 29, 30, 31, 32], 1, 4) == [29, 31]
        assert functions_py.prime([1, 9, 12, 2, 3, 5, 6], 3, 6) == [2, 3, 5]
        assert functions_py.prime([4, 6, 8, 2], 2, 4) == [2]
        assert functions_py.prime([17, 19, 23, 24], 0, 1) == [17]


        st = int(input("Enter the index you want to start from: "))
        dr = int(input("Enter the index where you want to end: "))


        functions_py.prime(lst, st, dr)

        print('\n')

    if q == "7":  # Odd function
        assert functions_py.odd([7, 6, 5, 4], 0, 3) == [7, 5]
        assert functions_py.odd([1, -3, 3, 2, 4, 8, 9, 11], 0, 4) == [1, -3, 3]
        assert functions_py.odd([9, 11, 12, 14], 0, 3) == [9, 11]
        assert functions_py.odd([8, 6, 4, 2], 0, 2) == []
        assert functions_py.odd([5, 15, 25], 0, 3) == [5, 15, 25]

        get_odd = []


        st = int(input("Enter the index you want to start from: "))
        dr = int(input("Enter the index where you want to end: "))


        get_odd = functions_py.odd(lst, st, dr)
        print(get_odd)

        print('\n')

    if q == "8":  # Sum function
        assert functions_py.suma([1, 2, 3, 4], 0, 4) == 10
        assert functions_py.suma([10, 20, 30], 0, 3) == 60
        assert functions_py.suma([-1, 1, 0], 0, 2) == 0
        assert functions_py.suma([100, 200], 1, 2) == 200
        assert functions_py.suma([5, -5, 10, -10], 2, 4) == 0


        st = int(input("Enter the index you want to start from: "))
        dr = int(input("Enter the index where you want to end: "))


        print(functions_py.suma(lst, st, dr))

        print('\n')

    if q == "9":  # GCD function
        assert functions_py.gcd_make([9, 27, 45], 0, 2) == 9
        assert functions_py.gcd_make([12, 18, 24], 0, 2) == 6
        assert functions_py.gcd_make([2, 56, 72, 104, 112, 95], 1, 4) == 8
        assert functions_py.gcd_make([3, 5, 7], 1, 2) == 1
        assert functions_py.gcd_make([100, 200, 300], 0, 1) == 100

        st = int(input("Enter the index you want to start from: "))
        dr = int(input("Enter the index where you want to end: "))

        print(functions_py.gcd_make(lst, st, dr))

        print('\n', 9)

    if q == "10":  # Maximum function
        assert functions_py.maxi([1, 942883, 94288383, 4], 1, 3) == 94288383
        assert functions_py.maxi([100, 50, 75, 90, 73, 129, 539, 939, 1001], 4, 9) == 1001
        assert functions_py.maxi([1, 10, 5], 0, 0) == 1
        assert functions_py.maxi([-5, -1, -10], 0, 2) == -1
        assert functions_py.maxi([0, 0, 0], 0, 2) == 0


        st = int(input("Enter the index you want to start from: "))
        dr = int(input("Enter the index where you want to end: "))


        print(functions_py.maxi(lst, st, dr))

        print('\n')

    if q == "11.1":  # Filter Primes function
        assert functions_py.filter_primes([2, 3, 4, 5, 6]) == [2, 3, 5]
        assert functions_py.filter_primes([10, 11, 12, 13]) == [11, 13]
        assert functions_py.filter_primes([17, 19, 22]) == [17, 19]
        assert functions_py.filter_primes([1, 4, 9]) == []
        assert functions_py.filter_primes([29, 31, 33]) == [29, 31]

        functions_py.filter_primes(lst)

        print(lst, end='\n')

    if q == "11.2":  # Filter Negatives function
        assert functions_py.filter_negatives([10, -10, 20, -20]) == [-10, -20]
        assert functions_py.filter_negatives([1, -1, 2, -2]) == [-1, -2]
        assert functions_py.filter_negatives([-5, -15, 0, 5]) == [-5, -15]
        assert functions_py.filter_negatives([10, 20, 30]) == []
        assert functions_py.filter_negatives([-100, -200, 300]) == [-100, -200]

        functions_py.filter_negatives(lst)

        print(lst, end='\n')

