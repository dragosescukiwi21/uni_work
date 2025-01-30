from domain.plane import Plane
from domain.passengers import Passengers

class Service:
    def __init__(self, plane_repo, passenger_repo):
        self.passengers_list = passenger_repo
        self.plane_list = plane_repo

    def create_read_plane(self):
        number = int(input("Enter plane number: "))
        company = str(input("Enter company name: "))
        num_seats = int(input("Enter number of seats: "))
        destination = str(input("Enter destination: "))

        try:
            if any(plane.get_number() == number for plane in self.plane_list):
                raise ValueError(f"Plane with number {number} already exists.")
            else:
                plist = []

                n = int(input("-- Now enter the amount of passengers: "))
                for i in range(n):
                    name = input(f"-- Enter name of passenger ({i}): ")
                    last_name = input(f"-- Enter last name of passenger ({i}): ")
                    passport_num = input(f"-- Enter passport number for passenger ({i}): ")

                    plist.append(self.create_passenger(name, last_name, passport_num))

                    obj = Plane(number, company, num_seats, destination, plist)
                    self.plane_list.append(obj)

        except Exception as e:
            print(f"Error creating plane: {e}")


    def update_plane(self, given_numb, n, c, ns, dest):
        index = 0
        for plane in self.plane_list:
            if plane.get_number() == given_numb:
                plane.set_number(n)
                plane.set_company(c)
                plane.set_num_seats(ns)
                plane.set_destination(dest)

                break

            index += 1

    # We delete plane by number
    def delete_plane(self, number):
        for plane in self.plane_list:
            if plane.get_number() == number:
                self.plane_list.remove(plane)



    # CRUD for passengers
    def create_passenger(self, name, last_name, passport_num):
        try:
            if any(passenger.get_passport_num() == passport_num for passenger in self.passengers_list):
                raise ValueError(f"Passenger with passport number {passport_num} already exists.")
            else:
                obj = Passengers(name, last_name, passport_num)
                self.passengers_list.append(obj)
        except Exception as e:
            print(f"Error creating passenger: {e}")

    def read_passenger(self):
        name = str(input("Enter passenger name: "))
        last_name = str(input("Enter passenger last name: "))
        passport_num = int(input("Enter passport number: "))

        self.create_passenger(name, last_name, passport_num)

    def update_passenger(self, given_passport_num, name, last_name, passport_num):
        for passenger in self.passengers_list:
            if passenger.get_passport_num() == given_passport_num:
                passenger.set_name(name)
                passenger.set_last_name(last_name)
                passenger.set_passport_num(passport_num)

                break

    def delete_passenger(self, passport_num):
        self.passengers_list = [passenger for passenger in self.passengers_list if passenger.get_passport_num() != passport_num]
