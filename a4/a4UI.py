class UI:
    def __init__(self, controller, repo):
        # Constructor initializes the UI with a controller and a repository.
        # `controller` is used to handle vector operations (CRUD).
        # `repo` provides access to storage and operations on vectors.
        self.controller = controller
        self.repo = repo

    @staticmethod
    def display_options():
        # Static method to display a list of available menu options for the user.
        operations = [
            "1  Create a new vector",
            "2  View all vectors",
            "3  View a vector by index",
            "4  Update a vector by index",
            "5  Update a vector by ID",
            "6  Delete a vector by index",
            "7  Delete a vector by ID",
            "8  Plot all vectors",
            "9  Sum values of vectors with the same color",
            "10  Delete all vectors",
            "11  Update color of a vector by ID",
            "0  Exit"
        ]

        print("\nSelect an operation:")
        for operation in operations:
            print(operation)
        print()

    def menu(self):
        # Main menu loop that displays options, takes user input, and performs operations accordingly
        while True:
            self.display_options()  # Show the menu options
            choice = int(input("Enter the number of the operation you want to perform (1-11): "))

            if choice == 0:
                # Exit the menu loop
                break

            elif choice == 1:
                # Option to create new vectors
                n = int(input("Enter the number of entries: "))  # Number of vectors to create

                for i in range(n):
                    # Gather vector attributes from the user
                    id = input("Enter the vector's name ID (int or str): ")
                    color = input("Enter the vector's color ('r', 'g', 'b', 'y', 'm'): ")
                    type = int(input("Enter the vector's type (>= 1): "))
                    vals = list(map(float, input("Enter the vector's values (space-separated): ").split(',')))

                    # Call the controller method to create the vector
                    self.controller.createVector(id, color, type, vals)
                    print()

            elif choice == 2:
                # Option to view all vectors.
                self.controller.printVectors()

            elif choice == 3:
                # Option to view a single vector by its index
                index = int(input("Enter the vector's index: "))
                self.controller.printVectorIndex(index)

            elif choice == 4:
                # Option to update a vector by its index
                index = int(input("Enter the vector's index: "))
                nid = input("Enter the new name ID: ")
                ncl = input("Enter the new color ('r', 'g', 'b', 'y', 'm'): ")
                nty = int(input("Enter the new type: "))
                nvals = list(map(float, input("Enter the new values (space-separated): ").split(',')))

                # Call the controller method to update the vector
                self.controller.updateVectorIndex(index, nid, ncl, nty, nvals)

            elif choice == 5:
                # Option to update a vector by its ID.
                id = input("Enter the ID of the vector to update: ")
                nid = input("Enter the new name ID: ")
                ncl = input("Enter the new color ('r', 'g', 'b', 'y', 'm'): ")
                nty = int(input("Enter the new type: "))
                nvals = list(map(float, input("Enter the new values (space-separated): ").split(',')))

                # Call the controller method to update the vector
                self.controller.updateVectorID(id, nid, ncl, nty, nvals)

            elif choice == 6:
                # Option to delete a vector by its index
                index = int(input("Enter the index of the vector to delete: "))
                self.controller.deleteVectorIndex(index)

            elif choice == 7:
                # Option to delete a vector by its ID
                id = input("Enter the ID of the vector to delete: ")
                self.controller.deleteVectorID(id)

            elif choice == 8:
                # Option to plot all vectors. No additional input is required
                self.repo.plot_vectors()

            elif choice == 9:
                # Option to sum values of vectors with the same color.
                col = input("Enter the color to sum values for: ")
                result = self.repo.sum_same_col(col)  # Call repository method to sum values

                print(result)

            elif choice == 10:
                # Option to delete all vectors from the repository
                self.repo.del_all_vectors()

            elif choice == 11:
                # Option to update the color of a vector by its ID.
                vec_id = input("Enter the ID of the vector: ")
                col = input("Enter the new color ('r', 'g', 'b', 'y', 'm'): ")
                self.repo.update_col_byID(vec_id, col)  # Call repository method to update color.

            else:
                # Handle invalid menu options.
                print("Invalid choice. Please try again.")
