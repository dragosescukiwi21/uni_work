# a number of the form xy where (xy)^2 = y is valid if (y^2) % 10 = y

lista = [0, 1, 5, 6]
for i in range (0, 100):
    for j in lista:
        if i % 10 == j:
            print(i)
