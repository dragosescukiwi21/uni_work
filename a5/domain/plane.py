class Plane:
    def __init__(self, number, company, num_seats, destination, passenger_repo):
        try:
            if not isinstance(number, int):
                raise TypeError("Number must be an integer.")


            if not isinstance(company, str):
                raise TypeError("Company must be a string.")


            if not isinstance(num_seats, int):
                raise TypeError("Number of seats must be an integer.")


            if not isinstance(destination, str):
                raise TypeError("Destination must be a string.")

            self.number = number
            self.company = company
            self.num_seats = num_seats
            self.destination = destination

            # We connect the plane with the passenger from the passenger list
            self.passenger_list = passenger_repo

        except TypeError as e:
            print(f"Error: {e}")



    def get_passenger_list(self):
        return self.passenger_list

    def get_number(self):
        return self.number

    def get_company(self):
        return self.company

    def get_num_seats(self):
        return self.num_seats

    def get_destination(self):
        return self.destination

    def set_number(self, val):
        self.number = val

    def set_company(self, val):
        self.company = val

    def set_num_seats(self, val):
        self.num_seats = val

    def set_destination(self, val):
        self.destination = val



class PlaneRepository:
    def __init__(self, plane_list):
        try:
            if not isinstance(plane_list, list):
                raise TypeError("Passenger list must be a list.")

            self.repo = plane_list

        except TypeError as e:
            print(f"Error: {e}")

    def __iter__(self):
        return iter(self.repo)
    def get_plist(self):
        return self.repo


    # 4) We sort the repository based on the number of passengers
    def sort_by_passengers_num(self):
        n = len(self.repo)

        for i in range(n):
            for j in range(i + 1, n):
                if len(self.repo[i].get_passenger_list()) > len(self.repo[j].get_passenger_list()):
                    aux = self.repo[i]
                    self.repo[i] = self.repo[j]
                    self.repo[j] = aux

    # 5) We iterate through passengers and count how many have the given substring in their full name. After that sort
    def sort_by_substring(self, substring):
        def count_substring_in_passenger_names(plane):
            count = 0
            for passenger in plane.get_passenger_list():
                if substring in passenger.get_name():
                    count += 1

            return count

        self.repo.sort(key=count_substring_in_passenger_names)


    # 6) We sort the repository based on the concatenation of seat number and destination
    def sort_by_concat(self):
        n = len(self.repo)

        concatList = []

        # We create a list of concatenated strings
        for plane in self.repo:
            concatList.append(f'{plane.num_seats}{plane.destination}')

        # We sort the repo based on the concatenated strings
        for i in range(n):
            for j in range(i + 1, n):
                if concatList[i] > concatList[j]:
                    aux = self.repo[i]
                    self.repo[i] = self.repo[j]
                    self.repo[j] = aux

    # 7) We check pairs of passengers to identify how many share the same first 3 digits in their passport number
    def identify_passenger_passport(self):
        c = 0

        for plane in self.repo:
            for i, passenger1 in enumerate(plane.get_passenger_list()):
                for passenger2 in plane.get_passenger_list()[i + 1:]:   # Here we iterate through the list starting from the next passenger

                    if passenger1.get_passport_num()[:3] == passenger2.get_passport_num()[:3]:
                        c += 1

        return c

    # 8) We iterate through passengers and count how many have the given substring in either their first or last name
    def identify_passenger_name_substring(self, substring):
        c = 0

        for plane in self.repo:
            for passenger in plane.get_passenger_list():
                if substring in passenger.get_name() or substring in passenger.get_last_name():
                    c += 1

        return c

    # 9) We iterate through passengers to check if their first and last name match the given names, and count matches
    def identify_passenger_name(self, first_name, last_name):
        c = 0

        for plane in self.repo:
            for passenger in plane.get_passenger_list():
                if passenger.get_name() == first_name and passenger.get_last_name() == last_name:
                    c += 1

        return c

    # 10) Form groups of k passengers from the same plane but with different last names by using backtracking
    def form_groups_of_k_passengers(self, k):
        def backtrack(start, group):
            # If it's a solution (its length is k) we append a copy to the list of results
            if len(group) == k:
                v.append(group[:])
                return

            # Classical backtracking with freq vector (last_names to keep track of who we put group).
            for i in range(start, len(passengers)):
                if passengers[i].get_last_name() not in last_names:
                    last_names.append(passengers[i].get_last_name())

                    group.append(passengers[i])

                    # We move to the next position and pop the last element after we come back from the recursion
                    backtrack(i + 1, group)
                    group.pop()

                    last_names.remove(passengers[i].get_last_name())


        # We initialize parameters and start backtracking. We will do this with each plane from our repo
        v = []
        for plane in self.repo:
            passengers = plane.get_passenger_list()
            last_names = []
            backtrack(0, [])

        return v

    # 11) Form groups of k planes with the same destination but belonging to different airline companies.
    def form_groups_of_k_planes(self, k, dest):
        main_list = self.get_plist()

        def backtrack(start, group):
            # If it's a solution (its length is k) we append a copy to the list of results
            if len(group) == k:
                v.append(group[:])
                return

            # Classical backtracking with freq vector (this time we want the planes and companies not to be repeated)
            for i in range(start, len(self.repo)):

                if main_list[i] not in plane_list and main_list[i].get_destination() == dest and main_list[i].get_company() not in company_list:
                    plane_list.append(main_list[i])
                    company_list.append(main_list[i].get_company())

                    group.append(main_list[i])

                    # We move to the next position and pop the last elements after we come back from the recursion
                    backtrack(i + 1, group)
                    group.pop()

                    plane_list.remove(main_list[i])
                    company_list.remove(main_list[i].get_company())

        # We initialize and start backtracking right off. This time we will be going only through the list of planes
        v = []
        plane_list = []
        company_list = []

        backtrack(0, [])
        return v


