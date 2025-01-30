import classes
import ui
from read import readStart
from tests import runTests

# Create the repository
listOfPoints = []
repo = classes.PointRepository(listOfPoints)


# We start reading in our repository and run tests to confirm everything is ok
readStart(repo)
runTests()


# Opening menu and connecting user's choices to the functions until they break the loop by selecting "0. Quit"
while True:
    ui.display_menu()
    choice = ui.get_user_input()

    if choice == 0:
        break

    elif choice == 1:
        x = float(input("Enter the x coordinate: "))
        y = float(input("Enter the y coordinate: "))
        col = str(input("Enter the color of the point: "))

        obj = classes.Point(x, y, col)
        repo.addPoint(obj)

    elif choice == 2:
        repo.printAllPoints()

    elif choice == 3:
        index = int(input("Enter the index of the point: "))
        point = repo.getPointAtIndex(index)

        print(point)

    elif choice == 4:
        color = str(input("Enter the color of the points to retrieve: "))

        repo.getPointsOfColor(color)

    elif choice == 5:
        x = float(input("Enter the (x) coordinate of the upper left corner point: "))
        y = float(input("Enter the (y) coordinate of the upper left corner point: "))
        color = str(input("Enter the point's color of the upper left corner point: "))

        length = int(input("Enter the length of the square: "))

        obj = classes.Point(x, y, color)
        repo.getPointsInsideSquare(obj, length)

    elif choice == 6:
        print(repo.getMinDistance())

    elif choice == 7:
        index = int(input("Enter the index of the point to update: "))
        new_x = float(input("Enter the new x coordinate: "))
        new_y = float(input("Enter the new y coordinate: "))
        new_col = str(input("Enter the new color: "))

        repo.updateByIndex(index, new_x, new_y, new_col)

    elif choice == 8:
        index = int(input("Enter the index of the point to delete: "))
        repo.deleteByIndex(index)

    elif choice == 9:
        x = float(input("Enter the (x) coordinate of the upper left corner point: "))
        y = float(input("Enter the (y) coordinate of the upper left corner point: "))
        color = str(input("Enter the point's color of the upper left corner point: "))

        length = int(input("Enter the length of the square: "))

        obj = classes.Point(x, y, color)
        repo.delPointsInsideSquare(obj, length)

    elif choice == 10:
        repo.plotAllPoints()

    elif choice == 11:
        print(repo.getMaxDistance())

    elif choice == 12:
        repo.shiftPointsOnX()

    elif choice == 13:
        x = float(input("Enter the (x) coordinate of the point of the circle center: "))
        y = float(input("Enter the (y) coordinate of the point of the circle center: "))
        color = str(input("Enter the point's color of the point: "))

        radius = float(input("Enter the radius of the circle: "))

        obj = classes.Point(x, y, color)
        repo.delPtsInsideCircle(obj, radius)
