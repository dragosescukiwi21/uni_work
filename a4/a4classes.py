import matplotlib as plt
import numpy as np

lista = []
c_accepted = ['r', 'g', 'b', 'y', 'm']

class myVector:
    def __init__(self, id, color, type, values):
        self.id = 0
        self.color = ''
        self.type = type

        try:
            if isinstance(id, (int, str)):
                self.id = id
            else:
                raise ValueError("Name ID has to be int or str")
        except ValueError as e:
            print(f"The program exited because: {e}")

        try:
            if color in c_accepted and isinstance(color, str):
                self.color = color
            else:
                raise ValueError("Color is not accepted")
        except ValueError as e:
            print(f"The program exited because: {e}")

        try:
            if type >= 1:
                self.type = type
            else:
                raise ValueError("Type has to be greater or equal to 1")
        except ValueError as e:
            print(f"The program exited because: {e}")

        self.values = values


    def __str__(self):
        return f'Vector {self.id} of color {self.color}, type {self.type} and values: {self.values}'

    # Get - Set
    def getNameId(self):
        return self.id

    def getColor(self):
        return self.color

    def getType(self):
        return self.type

    def getValues(self):
        return self.values

    def setNameID(self, val):
        self.id = val

    def setColor(self, val):
        self.color = val

    def setType(self, val):
        self.type = val

    def setValues(self, lista):
        self.values = lista


    # Problems
    # Adds a scalar value to the element at a specified index in the vector. Ensures the scalar is a numeric type (int or float)
    # If the scalar is invalid, raises a ValueError
    def add_scalar(self, index, scalar):
        try:
            if isinstance(scalar, (int, float)):
                self.values[index] += scalar
            else:
                raise ValueError("The value has to be greater or equal to 0")
        except ValueError as e:
            print(f"The program exited because: {e}")

    # Adds another vector to the current vector element-wise. Assumes that `other` is a vector with the same length
    def add_vector(self, other):
        for i in range(len(self.values)):
            self.values = self.values[i] + other.getValues()[i]

    # Subtracts another vector from the current vector element-wise. Assumes that `other` is a vector with the same length
    def sub_vector(self, other):
        for i in range(len(self.values)):
            self.values = self.values[i] - other.getValues()[i]

    # Calculates the sum of all elements in the vector. Uses NumPy's sum function for efficiency
    def sum_val(self):
        return np.sum(self.values)

    # Calculates the product of all elements in the vector. Uses NumPy's prod function for efficiency
    def prod(self):
        return np.prod(self.values)

    # Calculates the average (mean) of the vector's values. Ensures that the vector contains at least one value
    # Raises a ValueError if the vector is empty
    def avg(self):
        try:
            if len(self.values) == 0:
                raise ValueError("The vector has to have at least one value")
            else:
                return np.mean(self.values)
        except ValueError as e:
            print(f"The program exited because: {e}")

    # Finds and returns the minimum value in the vector, raises a ValueError if the vector is empty
    def min(self):
        if len(self.values) == 0:
            raise ValueError("The vector must have at least one value.")
        return np.min(self.values)

    # Finds and returns the maximum value in the vector and Ensures the vector has at least one value before proceeding
    def max(self):
        try:
            if len(self.values) > 0:
                return np.max(self.values)
            else:
                raise ValueError("The vector must have at least one value.")
        except ValueError as e:
            print(f"The program exited because: {e}")


class myVectorRepository:

    def __init__(self, vectorList):
        self.vectors = vectorList

    # We append the object to the repository list
    def add(self, vector):
        self.vectors.append(vector)

    # We return the list of objects within the repository
    def get_vectors(self):
        return self.vectors


    # We check for the index to be within bounds and we return the object at index if so
    def get_vector_index(self, index):
        try:
            if 0 >= index <= len(self.vectors):
                return self.vectors[index]
            else:
                raise ValueError("Index out of range")

        except ValueError as e:
            print(f"The program exited because: {e}")


    # !! the following update/delete functions are here for the sake of completing the assignment's requirements.
    # !! For the actual program's functionality, these are handled in Controller which is supposed to make use of these
    # !! type of CRUD operations.

    # Firstly we check that the values are compliant after which we use a try-except block to update the obj at i
    # or raise an error otherwise
    def update_vector_index(self, given_i, nid, ncl, nty, nvals):
        try:
            if 0 >= given_i <= len(self.vectors):
                self.vectors[given_i] = myVector(nid, ncl, nty, nvals)
            else:
                raise ValueError("Values not compliant")
        except ValueError as e:
            print(f"The program exited because: {e}")


    # We do the same as above but in this case by checking the id
    def update_vector_id(self, given_id, nid, ncl, nty, nvals):
        try:
            if isinstance(id, (int, str)):
                for vec in self.vectors:
                    if vec.getNameId() == given_id:
                        vec.setColor(ncl)
                        vec.setType(nty)
                        vec.setValues(nvals)

                        break
            else:
                raise ValueError("Values not compliant")
        except ValueError as e:
            print(f"The program exited because: {e}")


    # Here we simply delete the object at index "i"
    def del_index(self, i):
        try:
            if 0 >= i <= len(self.vectors) or isinstance(id, (int, str)):
                del self.vectors[i]
            else:
                raise IndexError("Index out of range")
        except ValueError as e:
            print(f"The program exited because: {e}")


    # Same as above but for id
    def del_id(self, id):
        try:
            if isinstance(id, (int, str)):
                for vec in self.vectors:
                    if vec.getNameId() == id:
                        del vec
                        break
            else:
                raise ValueError("Id is not valid")
        except ValueError as e:
            print(f"The program exited because: {e}")


    # Here we will plot the points of x = values[], y = index and the program will draw a line (vector) thru them
    def plot_vectors(self):
        mrk = ''
        list = self.get_vectors()

        for i in range(len(list)):
            x_list = []
            nr = len(list[i].getValues())

            while nr != 0:
                x_list.append(i)
                nr -= 1
            if list[i].getType() == 1:
                mrk = 'o'
            else:
                if list[i].getType() == 2:
                    mrk = 's'
                else:
                    if list[i].getType() == 3:
                        mrk = '^'
                    else:
                        if list[i].getType() >= 4:
                            mrk = 'D'
            plt.plot(x_list, list[i].get_values(), color=list[i].getColor(), marker=mrk)

        plt.show()

    # We search in our list of objects the given color and we add their values to a sum using the function given in iteration 1
    def sum_same_col(self, col):
        s = 0

        for vec in self.vectors:
            if vec.getColor() == col:
                s += myVector.sum_val(vec)

        return s


    # Here we update our object list with a newly emptied list, therefore deleting all previous objects
    def del_all_vectors(self):
        newlist = []
        self.vectors = newlist


    # We search in our list of objects the given ID and update the color with the setter for color
    def update_col_byID(self, id, col):
        for vec in self.vectors:
            if vec.getNameId() == id:
                vec.setColor(col)

                break
