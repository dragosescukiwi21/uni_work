import matplotlib.pyplot as plt
import numpy as np

color_accepted = {"red", "green", "blue", "yellow", "magenta"}

class Point:
    def __init__(self, x, y, color):
        # We check for x to be of type int or float, else we raise an error to the user
        try:
            if isinstance(x, (int, float)):
                self.__x = x
            else:
                raise TypeError("x must be of type int or float")
        except TypeError as e:
            print(f"The program exited because: {e}")

        # We check for y to be of type int or float, else we raise an error to the user
        try:
            if isinstance(y, (int, float)):
                self.__y = y
            else:
                raise TypeError("y must be of type int or float")
        except TypeError as e:
            print(f"The program exited because: {e}")

        # We check for color to be a string, else we raise an error to the user
        try:
            if isinstance(color, str) and color in color_accepted:
                self.__color = color
            else:
                raise TypeError("y must be of type int or float")
        except TypeError as e:
            print(f"The program exited because: {e}")

    # We make this the default print (when we print, it outputs out this string)
    def __str__(self):
        return f"Point({self.__x}, {self.__y} of color {self.__color})"

    # Get + Set
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getColor(self):
        return self.__color

    # Check for value to be of type int or float for x
    def setX(self, val):
        try:
            if isinstance(val, (int, float)):
                self.__x = val
            else:
                raise ValueError("x is not a number")
        except ValueError:
            print(f"Error setting x: {ValueError}")

    # Check for value to be of type int or float for y
    def setY(self, val):
        try:
            if isinstance(val, (int, float)):
                self.__y = val
            else:
                raise ValueError("y is not a number")
        except ValueError as e:
            print(f"Error setting y: {e}")

    # Check for value to be of type str for color + checking the color is within the accepted list of colors
    def setColor(self, val):
        try:
            if isinstance(val, str):
                self.__color = val
            else:
                raise ValueError("color must be a string")

            x = False
            for c in color_accepted:
                if c == val:
                    x = True
            if not x:
                raise ValueError("color is not in accepted list")
        except ValueError as e:
            print(f"Error setting color: {e}")


class PointRepository:
    def __init__(self, PointList):
        self.__points = PointList

    # I added another essential function that prints our points through class Points (with the __str__ modifier)
    # This way we avoid printing with class PointRepository which would return the place in memory the object is
    def printAllPoints(self):
        for pts in self.__points:
            print(pts)

    # We add the object at the end of our repo
    def addPoint(self, obj):
        self.__points.append(obj)

    # We return the whole list of Point objects
    def getPoints(self):
        return self.__points

    # We return the object at index "index"
    def getPointAtIndex(self, index):
        # Checking for out-of-bound inputs
        if index >= len(self.__points) or index < 0:
            raise IndexError("Index out of range")
        elif not isinstance(index, int):
            raise IndexError("Index has to be int")
        else:
            return self.__points[index]

    # Iterating through our points list and returning the ones with color "color" through a list
    def getPointsOfColor(self, color):
        # Checking if the color is in accepted colors
        if color not in color_accepted:
            raise ValueError("Color must be in accepted list")
        else:
            ListOfColors = []

            for pts in self.__points:
                if pts.getColor() == color:
                    ListOfColors.append(pts)

            for pts in ListOfColors:
                print(pts)

    # We check for the point to be within the bound of our square
    def getPointsInsideSquare(self, point, length):
        lista = []
        for i in self.__points:
            # For each point we check it's X to be within the upper left corner's X and the other corner's X and
            # same for the Y coordinate

            if point.getX() <= i.getX() <= point.getX() + length:
                if point.getY() >= i.getY() >= point.getY() - length:
                    lista.append(i)

        for pts in lista:
            print(pts)

    # We check the distance for each point to all other points and compute the min.
    # Also, I used enumerate which is the same as "i in self.__points" but also keeps track of index which is easier
    def getMinDistance(self):
        min_dist = float('inf')  # This will set min as infinity so we can compare later
        n = len(self.__points)

        # Iterate through each point
        for i, pt1 in enumerate(self.__points):
            x1, y1 = pt1.getX(), pt1.getY()

            # Compare it to every other point
            for j, pt2 in enumerate(self.__points):
                if i == j:  # Skip the same point
                    continue
                else:
                    # Check for distance to be smaller than our min
                    x2, y2 = pt2.getX(), pt2.getY()
                    dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                    if dist < min_dist:
                        min_dist = dist

        return min_dist

    # We set new values for point at the given index
    def updateByIndex(self, index, new_x, new_y, new_color):
        # Checking index is an int
        if not isinstance(index, int):
            raise IndexError("index must be an integer")
        if index >= len(self.__points) or index < 0:
            raise ValueError("Index out of range")

        # Checking x and y to be int or float
        if isinstance(new_x, (int, float)):
            self.__points[index].setX(new_x)
        else:
            raise ValueError("x is not a number")

        if isinstance(new_y, (int, float)):
            self.__points[index].setY(new_y)
        else:
            raise ValueError("y is not a number")

        # Checking color to be a string and be in accepted colors
        if isinstance(new_color, str) and new_color in color_accepted:
            self.__points[index].setColor(new_color)
        else:
            raise ValueError("color is not a string")

    # We pop our object at index out of the repo
    def deleteByIndex(self, index):
        if not isinstance(index, int):
            raise IndexError("index must be an integer")
        elif index >= len(self.__points) or index < 0:
            raise ValueError("Index out of range")
        else:
            del self.__points[index]

    # Same as for getPointsInsideSquare but this time we remove the from the repository
    def delPointsInsideSquare(self, point, length):
        for i in self.__points:
            if point.getX() <= i.getX() <= point.getX() + length:
                if point.getY() >= i.getY() >= point.getY() - length:
                    self.__points.remove(i)

    # We draw the points and then we show them using matplotlib
    def plotAllPoints(self):
        for pts in self.__points:
            # Drawing all points on the repository
            plt.scatter(pts.getX(), pts.getY(), c=pts.getColor())

        plt.show()

    # We check the distance for each point to all other points and compute the max.
    # Just like getMinDistance but for max
    def getMaxDistance(self):
        max_dist = 0
        n = len(self.__points)

        for i, pt1 in enumerate(self.__points):
            x1, y1 = pt1.getX(), pt1.getY()

            for j, pt2 in enumerate(self.__points):
                if i == j:
                    continue
                else:
                    x2, y2 = pt2.getX(), pt2.getY()
                    dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                    if dist > max_dist:
                        max_dist = dist

        return max_dist

    # We change all y to 0 so that all the points lie on the X axis
    def shiftPointsOnX(self):
        for pts in self.__points:
            pts.setY(0)

    # We consider "Center" a point in the center of the circle and "Radius" the distance from the center of the circle
    # and any point on the border of the circle
    def delPtsInsideCircle(self, center, radius):
        if radius < 0 or radius >= len(self.__points):
            raise ValueError("radius must be within bounds")
        else:
            index = 0
            for i in self.__points:
                # We compute, for any point in points, their distance to the center of the circle
                dist = np.sqrt((i.getX() - center.getX()) ** 2 + (i.getY() - center.getY()) ** 2)

                # We delete it if it's inside the circle
                if dist < radius:
                    del self.__points[index]

                # Testing case where center is a given point in the repository (it doesn't delete)
                if i.getX() == center.getX() and i.getY() == center.getY():
                    del self.__points[index]

                index += 1
