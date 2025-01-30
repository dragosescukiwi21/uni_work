import classes
def display_menu():
    operations = [
        "0. To exit",
        "1. Add a point to the repository",
        "2. Get all points",
        "3. Get a point at a given index",
        "4. Get all points of a given color",
        "5. Get all points that are inside a given square (up-left corner and length given)",
        "6. Get the minimum distance between two points",
        "7. Update a point at a given index",
        "8. Delete a point by index",
        "9. Delete all points that are inside a given square",
        "10. Plot all points in a chart (using matplotlib)",
        "11. Get the maximum distance between two points",
        "12. Shift all points on the x axis",
        "13. Delete all points that are inside a given circle",
    ]

    print("\nSelect an operation:")
    for operation in operations:
        print(operation)

    print()

def get_user_input():
    choice = int(input("Enter the number of the operation you want to perform (1-13): "))
    if choice < 0 or choice > 13:
        raise ValueError("Please enter a number between 1 and 13")
    else:
        return choice
