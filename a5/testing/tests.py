import unittest
from domain.plane import PlaneRepository, Plane
from domain.passengers import Passengers, PassengerRepository


class Test(unittest.TestCase):

    def setUp(self):

        # Sample data for planes and passengers
        self.passenger1 = Passengers("Ion", "Popescu", "123456")
        self.passenger2 = Passengers("Maria", "Ionescu", "123789")
        self.passenger3 = Passengers("Ana", "Georgescu", "456123")

        self.plane1 = Plane(1, "Dragos Fly", 100, "Bucuresti", [self.passenger1, self.passenger2])
        self.plane2 = Plane(2, "COSMIN SRL", 150, "Cluj-Napoca", [self.passenger3])

        self.repo = PlaneRepository([self.plane1, self.plane2])

        self.p_repo = PassengerRepository([self.passenger1, self.passenger2, self.passenger3])


    def tearDown(self):
        self.repo = None


    def test_sort_ln(self):
        self.p_repo.sort_ln()

        passengers = self.p_repo.get_repo()

        self.assertEqual(passengers[0].get_last_name(), "Georgescu")
        self.assertEqual(passengers[1].get_last_name(), "Ionescu")
        self.assertEqual(passengers[2].get_last_name(), "Popescu")

        # Verify the repository length remains unchanged
        self.assertEqual(len(passengers), 3)

    def test_sort_by_passengers_num(self):
        self.repo.sort_by_passengers_num()
        self.assertEqual(self.repo.repo[0], self.plane2)  # Plane with fewer passengers first
        self.assertEqual(self.repo.repo[1], self.plane1)
        self.assertNotEqual(self.repo.repo[0], self.plane1)
        self.assertNotEqual(self.repo.repo[1], self.plane2)
        self.assertEqual(len(self.repo.repo), 2)

    def test_sort_by_substring(self):
        self.repo.sort_by_substring("Io")

        # Get the counts of passengers with names containing "Io" for each plane
        plane_0_count = sum(1 for passenger in self.repo.repo[0].get_passenger_list() if "Io" in passenger.get_name())
        plane_1_count = sum(1 for passenger in self.repo.repo[1].get_passenger_list() if "Io" in passenger.get_name())


        self.assertEqual(plane_0_count, 0)
        self.assertEqual(plane_1_count, 1)
        self.assertIsInstance(plane_0_count, int)
        self.assertIsInstance(plane_1_count, int)
        self.assertEqual(len(self.repo.repo), 2)


    def test_sort_by_concat(self):
        self.repo.sort_by_concat()
        self.assertEqual(self.repo.repo[0], self.plane1)  # Based on concatenation of seat number and destination
        self.assertNotEqual(self.repo.repo[1], self.plane1)
        self.assertEqual(len(self.repo.repo), 2)
        self.assertIsInstance(self.repo.repo[0], Plane)
        self.assertIsInstance(self.repo.repo[1], Plane)

    def test_identify_passenger_passport(self):
        count = self.repo.identify_passenger_passport()

        self.assertEqual(count, 1)  # Passengers 1 and 2 share "123" prefix
        self.assertNotEqual(count, 0)
        self.assertGreaterEqual(count, 0)
        self.assertIsInstance(count, int)
        self.assertLessEqual(count, len(self.repo.repo[0].get_passenger_list()) + len(self.repo.repo[1].get_passenger_list()))

    def test_identify_passenger_name_substring(self):
        count = self.repo.identify_passenger_name_substring("Ionescu")
        self.assertEqual(count, 1)  # Only Maria Ionescu matches
        self.assertNotEqual(count, 0)
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)
        self.assertLessEqual(count, len(self.repo.repo[0].get_passenger_list()) + len(self.repo.repo[1].get_passenger_list()))

    def test_identify_passenger_name(self):
        count = self.repo.identify_passenger_name("Maria", "Ionescu")

        self.assertEqual(count, 1)  # Maria Ionescu matches
        self.assertNotEqual(count, 0)
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)
        self.assertLessEqual(count, len(self.repo.repo[0].get_passenger_list()) + len(self.repo.repo[1].get_passenger_list()))

    def test_form_groups_of_k_passengers(self):
        groups = self.repo.form_groups_of_k_passengers(2)

        self.assertEqual(len(groups), 1)

        self.assertEqual([p.get_last_name() for p in groups[0]], ["Popescu", "Ionescu"])

        self.assertNotIn("Popescu", [p.get_last_name() for p in groups[0][1:]])
        self.assertNotIn("Ionescu", [p.get_last_name() for p in groups[0][:-1]])

        self.assertTrue(all(passenger in self.plane1.get_passenger_list() for passenger in groups[0]))

        self.assertTrue(all(len(group) == 2 for group in groups))


    def test_form_groups_of_k_planes(self):
        groups = self.repo.form_groups_of_k_planes(1, "Cluj-Napoca")

        self.assertEqual(len(groups), 1)

        self.assertEqual(groups[0][0].get_number(), 2)
        self.assertEqual(groups[0][0].get_company(), "COSMIN SRL")
        self.assertEqual(groups[0][0].get_destination(), "Cluj-Napoca")

        self.assertTrue(len(set([plane.get_company() for plane in groups[0]])) == len(groups[0]))

        self.assertTrue(all(plane.get_destination() == "Cluj-Napoca" for plane in groups[0]))
        self.assertTrue(all(len(group) == 1 for group in groups))

# Function to run the tests
def runTests():
    # Unittest has a built in option to load all tests. We will store these in x
    x = unittest.TestLoader().loadTestsFromTestCase(Test)

    # We start the test and run it (again with the built in options from unittest)
    runner = unittest.TextTestRunner()
    runner.run(x)


if __name__ == "__main__":
    runTests()
