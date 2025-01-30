class UI:
    def __init__(self, controller, repository, psg_repo):
        self.controller = controller

        self.repository = repository
        self.psg_repo = psg_repo

    @staticmethod
    def display_menu():
        print("\nPlane Repository Operations")
        print("a. Add a plane (with passengers)")
        print("b. Remove a plane")
        print("1. Sort Passengers by Last Name")
        print("2. Sort Planes According to Number of Passengers")
        print("3. Sort Planes by Passenger Number and First Name Substring")
        print("4. Sort Planes According to the Concat. of Passenger Names and Destinations")
        print("5. Count by Passports That Start with the Same 3 Digits/Letters")
        print("6. Count by Substring in Passenger Names")
        print("7. Count by Full Name")
        print("8. Form Groups of K Passengers")
        print("9. Form Groups of K Planes With Given Destination")
        print("-------------------")
        print("10. Exit")

    def run(self):
        while True:


            self.display_menu()
            choice = input("Enter what operation you would like to make: ")



            if choice == "a":
                self.controller.create_read_plane()

            if choice == "b":
                i = input("Enter plane index: ")

                # plane [i] is meant to have passengers [i] as well so we delete them both
                self.controller.delete_plane(i)
                self.controller.delete_passenger(i)





            if choice == "1":
                # Here we could've used the plane repo to sort but why not do it like this :p
                self.psg_repo.sort_ln()

            if choice == "2":
                self.repository.sort_by_passengers_num()

            elif choice == "3":
                self.repository.sort_by_substring()

            elif choice == "4":
                self.repository.sort_by_concat()

            elif choice == "5":
                print(self.repository.identify_passenger_passport())

            elif choice == "6":
                print(self.repository.identify_passenger_name_substring())

            elif choice == "7":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                print(self.repository.identify_passenger_name(first_name, last_name))

            elif choice == "8":
                k = input("Enter k: ")
                print(self.repository.form_groups_of_k_passengers(k))

            elif choice == "9":
                k = input("Enter k: ")
                destination = input("Enter destination: ")

                print(self.repository.form_groups_of_k_planes(k, destination))

            elif choice == "10":
                break

            else:
                print("Invalid option. Please try again.")
