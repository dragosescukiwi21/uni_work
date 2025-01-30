import classes

def readStart(repo):
    n = (int(input("Enter a number of points you want to add: ")))

    # We add the object created by our user in the repository
    for i in range(n):
        x = float(input("Enter the (x) coordinate: "))
        y = float(input("Enter the (y) coordinate: "))
        color = str(input("Enter the point's color: "))

        obj = classes.Point(x, y, color)
        repo.addPoint(obj)
