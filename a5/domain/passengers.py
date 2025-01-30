class Passengers:
    def __init__(self, name, last_name, passport_num):
        self.name = name
        self.last_name = last_name
        self.passport_num = passport_num

    def __str__(self):
        print(f"Passenger: {self.name}, {self.last_name} and passport: {self.passport_num}")

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_passport_num(self):
        return self.passport_num

    def set_name(self, val):
        self.name = val

    def set_last_name(self, val):
        self.last_name = val

    def set_passport_num(self, val):
        self.passport_num = val


# !!!!! IMPORTANT !!!!!

# We will consider this repository as a framework for the passengers in the plane which means they will be connected
# (ith passengers from Plane = ith passengers from Passenger)
class PassengerRepository:
    def __init__(self, passengers_list):
        self.repo = passengers_list

    def __iter__(self):
        return iter(self.repo)

    def get_repo(self):
        return self.repo

    def sort_ln(self):
        n = len(self.repo)

        for i in range(n):
            for j in range(i + 1, n):
                if self.repo[i].get_last_name() > self.repo[j].get_last_name():
                    aux = self.repo[i]
                    self.repo[i] = self.repo[j]
                    self.repo[j] = aux

